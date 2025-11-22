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
from translations import translations
DEFAULT_LANG = "fr"

def t(lang: str, key: str) -> str:
    # Fallback si la langue ou la clé n’existe pas
    return translations.get(lang, translations[DEFAULT_LANG]).get(key, translations[DEFAULT_LANG].get(key, ""))
@app.get("/")
def inicio(lang: str = DEFAULT_LANG):
    return {"message": t(lang, "welcome")}
@app.post("/reports")
def crear_reporte(reporte: Reporte, lang: str = DEFAULT_LANG, db: Session = Depends(get_db)):
    # ... ta logique d’anonymisation et de sauvegarde ...
    nuevo = Denuncia(
        original_text=reporte.texto,
        anonymized_text=anon,
        tipo_abuso=reporte.tipo_abuso,
        idioma=reporte.idioma
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {
        "message": t(lang, "report_created"),
        "id": nuevo.id,
        "idioma": reporte.idioma
    }
@app.get("/reports/{id}")
def get_report(id: int, lang: str = DEFAULT_LANG, db: Session = Depends(get_db)):
    r = db.query(Denuncia).get(id)
    if not r:
        return {"error": t(lang, "error")}
    return {
        "message": t(lang, "success"),
        "report": {
            "id": r.id,
            "idioma": r.idioma,
            "tipo_abuso": r.tipo_abuso,
            "original_text": r.original_text,
            "anonymized_text": r.anonymized_text
        }
    }
from sqlalchemy import func

@app.get("/stats")
def get_stats(lang: str = DEFAULT_LANG, db: Session = Depends(get_db)):
    total = db.query(Denuncia).count()
    por_tipo = (
        db.query(Denuncia.tipo_abuso, func.count(Denuncia.id))
        .group_by(Denuncia.tipo_abuso)
        .all()
    )
    return {
        "message": t(lang, "stats"),
        "total": total,
        "por_tipo": {tipo: cantidad for tipo, cantidad in por_tipo}
    }
@app.get("/stats/export")
def export_stats(lang: str = DEFAULT_LANG, db: Session = Depends(get_db)):
    # ... génère le CSV depuis la base ...
    # Exemple de métadonnée traduite si tu renvoies un JSON de confirmation:
    return {"message": t(lang, "success")}
@app.get("/timeline")
def get_timeline(lang: str = DEFAULT_LANG, db: Session = Depends(get_db)):
    # ... construis tes jalons ...
    return {
        "message": t(lang, "success"),
        "timeline": hitos
    }
@app.get("/languages")
def get_languages(lang: str = DEFAULT_LANG):
    return {
        "message": t(lang, "success"),
        "supported": list(translations.keys())
    }
from abuse_types import abuse_types
from translations import translations

DEFAULT_LANG = "fr"

def t(lang: str, key: str) -> str:
    return translations.get(lang, translations[DEFAULT_LANG]).get(
        key, translations[DEFAULT_LANG].get(key, "")
    )

@app.get("/abuse-types")
def get_abuse_types(lang: str = DEFAULT_LANG):
    """
    Endpoint qui retourne la taxonomie des abus institutionnels
    dans la langue choisie (fr, es, en, sw, ln).
    """
    if lang not in abuse_types:
        lang = DEFAULT_LANG
    return {
        "message": t(lang, "success"),
        "types": list(abuse_types[lang].values())
    }
from abuse_types import abuse_types
from translations import translations

DEFAULT_LANG = "fr"

def t(lang: str, key: str) -> str:
    return translations.get(lang, translations[DEFAULT_LANG]).get(
        key, translations[DEFAULT_LANG].get(key, "")
    )

@app.get("/abuse-types")
def get_abuse_types(lang: str = DEFAULT_LANG):
    """
    Endpoint qui retourne la taxonomie des abus institutionnels
    dans la langue choisie (fr, es, en, sw, ln).
    Chaque entrée contient le code interne + la traduction.
    """
    if lang not in abuse_types:
        lang = DEFAULT_LANG
    return {
        "message": t(lang, "success"),
        "types": [
            {"code": code, "label": abuse_types[lang][code]}
            for code in abuse_types[lang].keys()
        ]
        }
from pydantic import BaseModel
from abuse_types import abuse_types
from translations import translations
import spacy

# Charger un modèle NLP multilingue (ex. spaCy)
# Tu peux installer : python -m spacy download xx_ent_wiki_sm
nlp = spacy.load("xx_ent_wiki_sm")

DEFAULT_LANG = "fr"

def t(lang: str, key: str) -> str:
    return translations.get(lang, translations[DEFAULT_LANG]).get(
        key, translations[DEFAULT_LANG].get(key, "")
    )

class Consulta(BaseModel):
    user: str
    question: str
    lang: str = "fr"

@app.post("/consultation")
def consultation(data: Consulta):
    lang = data.lang if data.lang in abuse_types else DEFAULT_LANG
    doc = nlp(data.question)

    # Normaliser la question
    q = data.question.lower()

    # Détection par similarité avec taxonomie
    detected = None
    for code, label in abuse_types[lang].items():
        if label.lower() in q:
            detected = (code, label)
            break
        # Vérification par tokens NLP
        for token in doc:
            if token.text.lower() in label.lower().split():
                detected = (code, label)
                break

    if detected:
        code, label = detected
        return {
            "message": t(lang, "success"),
            "interpretation": f"Votre question mentionne un abus de type: {label}",
            "suggestion": f"Vous pouvez créer une dénonciation avec le code interne '{code}' via /reports"
        }

    return {
        "message": t(lang, "success"),
        "interpretation": "Votre question est de nature générale",
        "suggestion": "Consultez les statistiques via /stats ou la liste des abus via /abuse-types"
    }
git commit -m "Add Hugging Face dependencies"
git push origin main
from pydantic import BaseModel
from abuse_types import abuse_types
from translations import translations
from transformers import pipeline

# Charger un pipeline multilingue
classifier = pipeline("text-classification", model="xlm-roberta-base", tokenizer="xlm-roberta-base")

DEFAULT_LANG = "fr"

def t(lang: str, key: str) -> str:
    return translations.get(lang, translations[DEFAULT_LANG]).get(
        key, translations[DEFAULT_LANG].get(key, "")
    )

class Consulta(BaseModel):
    user: str
    question: str
    lang: str = "fr"

@app.post("/consultation")
def consultation(data: Consulta):
    lang = data.lang if data.lang in abuse_types else DEFAULT_LANG

    # Classification Hugging Face
    result = classifier(data.question, truncation=True)[0]
    label = result["label"]
    score = result["score"]

    # Vérifier si le label correspond à un code interne
    if label in abuse_types[lang]:
        return {
            "message": t(lang, "success"),
            "interpretation": f"Votre question correspond à un abus de type: {abuse_types[lang][label]}",
            "confidence": f"{score:.2f}",
            "suggestion": f"Vous pouvez créer une dénonciation avec le code interne '{label}' via /reports"
        }

    return {
        "message": t(lang, "success"),
        "interpretation": "Votre question est de nature générale",
        "confidence": f"{score:.2f}",
        "suggestion": "Consultez les statistiques via /stats ou la liste des abus via /abuse-types"
}
git add .
git commit -m "API completa con frontend y logs"
git push origin main
git add main.py
git commit -m "Fix syntax error in main.py"
git push origin main
