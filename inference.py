from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import os

MODEL_NAME = os.getenv("MODEL_NAME")

def load_model_and_tokenizer(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return tokenizer, model

def predict_sentiment(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)

    with torch.no_grad():
        outputs = model(**inputs)

    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_label = torch.argmax(predictions, dim=1).item()
    confidence = predictions[0][predicted_label].item()

    return predicted_label, confidence

if __name__ == "__main__":
    tokenizer, model = load_model_and_tokenizer(MODEL_NAME)
    text = os.getenv("INPUT_TEXT")
    label, confidence = predict_sentiment(text, tokenizer, model)
    sentiment_map = {0: "Negative", 1: "Positive"}
    sentiment = sentiment_map[label]
    print(f"{sentiment}")
