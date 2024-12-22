FROM huggingface/transformers-pytorch-cpu:latest

WORKDIR /app

COPY inference.py .

# Pre-load the model during image build
RUN python3 -c "from transformers import AutoTokenizer, AutoModelForSequenceClassification; AutoTokenizer.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english'); AutoModelForSequenceClassification.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')"
