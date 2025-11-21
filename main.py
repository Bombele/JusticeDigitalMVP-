from fastapi import FastAPI, Form
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import spacy
import subprocess

# Cargar modelo spaCy (auto-download si falta)
try:
    nlp = spacy.load("es_core_news_sm")
except:
    subprocess.run(["python", "-m", "spacy", "download", "es_core_news_sm"])
    nlp = spacy.load("es_core_news_sm")

app = FastAPI()
Base = declarative_base()
engine = create_engine("sqlite:///denuncias.db")
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

class Denuncia(Base):
    __tablename__ = "denuncias"
    id = Column(Integer, primary_key=True, index=True)
    original_text = Column(Text)
    anonymized_text = Column(Text)
    tipo_abuso = Column(String)

Base.metadata.create_all(bind=engine)

class Reporte(BaseModel):
    texto: str
    tipo_abuso: str

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a JusticeDigitalMVP"}

@app.post("/anonymize")
def anonymize_text(texto: str = Form(...)):
    doc = nlp(texto)
    anon = texto
    for ent in doc.ents:
        anon = anon.replace(ent.text, f"[{ent.label_}]")
    return {"texto_anonimizado": anon}

@app.post("/reports")
def crear_reporte(reporte: Reporte):
    doc = nlp(reporte.texto)
    anon = reporte.texto
    for ent in doc.ents:
        anon = anon.replace(ent.text, f"[{ent.label_}]")
    nuevo = Denuncia(original_text=reporte.texto, anonymized_text=anon, tipo_abuso=reporte.tipo_abuso)
    session.add(nuevo)
    session.commit()
    return {"id": nuevo.id, "texto_anonimizado": anon}

@app.get("/reports/{id}")
def obtener_reporte(id: int):
    reporte = session.query(Denuncia).filter(Denuncia.id == id).first()
    if reporte:
        return {
            "id": reporte.id,
            "tipo_abuso": reporte.tipo_abuso,
            "texto_anonimizado": reporte.anonymized_text
        }
    return {"error": "Reporte no encontrado"}
from sqlalchemy import func
from fastapi import Depends

# Dependencia para obtener sesión en cada request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    total = db.query(Denuncia).count()
    por_tipo = db.query(Denuncia.tipo_abuso, func.count()).group_by(Denuncia.tipo_abuso).all()
    return {
        "total_denuncias": total,
        "por_tipo": {tipo: count for tipo, count in por_tipo}
    }
from sqlalchemy import func
from fastapi import Depends
import csv
import io
from fastapi.responses import StreamingResponse

# Dependencia para obtener sesión en cada request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    total = db.query(Denuncia).count()
    por_tipo = db.query(Denuncia.tipo_abuso, func.count()).group_by(Denuncia.tipo_abuso).all()
    return {
        "total_denuncias": total,
        "por_tipo": {tipo: count for tipo, count in por_tipo}
    }

@app.get("/stats/export")
def export_stats(db: Session = Depends(get_db)):
    por_tipo = db.query(Denuncia.tipo_abuso, func.count()).group_by(Denuncia.tipo_abuso).all()
    
    # Crear un buffer CSV en memoria
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Tipo de abuso", "Cantidad"])
    for tipo, count in por_tipo:
        writer.writerow([tipo, count])
    
    output.seek(0)
    return StreamingResponse(
        output,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=stats.csv"}
    )
from datetime import datetime

@app.get("/timeline")
def get_timeline(db: Session = Depends(get_db)):
    # Hitos fijos del proyecto
    hitos = [
        {"fecha": "2025-11-18", "evento": "Inicio del proyecto JusticeDigitalMVP"},
        {"fecha": "2025-11-19", "evento": "Primer endpoint de anonimización (/anonymize)"},
        {"fecha": "2025-11-20", "evento": "Integración de estadísticas (/stats) y exportación CSV"},
        {"fecha": "2025-11-21", "evento": "Diagnóstico de crash en Railway y resiliencia en GitHub"},
    ]

    # Denuncias emblemáticas (últimas 3)
    denuncias = db.query(Denuncia).order_by(Denuncia.id.desc()).limit(3).all()
    for d in denuncias:
        hitos.append({
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "evento": f"Denuncia #{d.id} registrada: {d.tipo_abuso}"
        })

    return {"timeline": hitos}
