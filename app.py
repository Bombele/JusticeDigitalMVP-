import gradio as gr

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
