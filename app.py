import gradio as gr
from abuse_types import abuse_types
def get_abuse_labels(lang="fr"):
    return [f"{item['code']} – {item[lang]}" for item in abuse_types]
# Fonction simple de démonstration
def classify_abus(text):
    # Ici tu pourras brancher ton modèle NLP (spaCy, Transformers, etc.)
    if "détention" in text.lower():
        return "Abus judiciaire"
    elif "corruption" in text.lower():
        return "Abus administratif"
    else:
        return "Type d'abus non identifié"

# Interface Gradio
iface = gr.Interface(
    fn=classify_abus,
    inputs="text",
    outputs="text",
    title="LexCivic – Signalement citoyen",
    description="Plateforme citoyenne de justice digitale pour classifier les abus institutionnels."
)

# Lancement
if __name__ == "__main__":
    iface.launch()
import gradio as gr
import spacy

# Charger un modèle multilingue spaCy (ex: français)
nlp = spacy.load("fr_core_news_sm")

# Fonction de classification simple
def classify_abus(text):
    doc = nlp(text)
    # Exemple rudimentaire basé sur mots-clés
    if "détention" in text.lower() or "prison" in text.lower():
        return "Abus judiciaire"
    elif "corruption" in text.lower() or "fraude" in text.lower():
        return "Abus administratif"
    elif "violence" in text.lower() or "police" in text.lower():
        return "Abus sécuritaire"
    else:
        return "Type d'abus non identifié"

# Interface Gradio
iface = gr.Interface(
    fn=classify_abus,
    inputs="text",
    outputs="text",
    title="LexCivic – Signalement citoyen",
    description="Plateforme citoyenne de justice digitale pour classifier les abus institutionnels."
)

if __name__ == "__main__":
    iface.launch()
import spacy
import subprocess

try:
    nlp = spacy.load("xx_ent_wiki_sm")
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", "xx_ent_wiki_sm"])
    nlp = spacy.load("xx_ent_wiki_sm")
import spacy
import subprocess

try:
    nlp = spacy.load("xx_ent_wiki_sm")
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", "xx_ent_wiki_sm"])
    nlp = spacy.load("xx_ent_wiki_sm")
import spacy
import subprocess

try:
    nlp = spacy.load("xx_ent_wiki_sm")
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", "xx_ent_wiki_sm"])
    nlp = spacy.load("xx_ent_wiki_sm")
