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
