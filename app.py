import gradio as gr
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

MODEL_PATH = "./model"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)


def predict(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=256
    )

    with torch.no_grad():
        outputs = model(**inputs)

    probs = torch.softmax(outputs.logits, dim=1)
    hate_prob = probs[0][1].item()

    prediction = "Hate Speech" if hate_prob > 0.35 else "Not Hate Speech"

    return {
        "prediction": prediction,
        "hate_probability": round(hate_prob, 4)
    }


demo = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(
        lines=4,
        placeholder="Enter Hindi, English or Hinglish text"
    ),
    outputs="json",
    title="Multilingual Hate Speech Detector",
    description="MuRIL fine-tuned on Hindi, English and Hinglish hate speech data"
)

demo.launch()