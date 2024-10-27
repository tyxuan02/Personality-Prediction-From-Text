# model_predictor.py
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn import functional as F
from mbti_labels import label_encoder

class ModelPredictor:
    def __init__(self, model_path='bert_model.pth', model_name='bert-base-uncased'):
        # Load tokenizer and model
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertForSequenceClassification.from_pretrained(model_name, num_labels=len(label_encoder.classes_))
        self.model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
        self.model.eval()
    
    def predict(self, text_input):
        # Tokenize the input text
        inputs = self.tokenizer(text_input, return_tensors="pt", padding=True, truncation=True)
        input_ids = inputs["input_ids"]
        attention_mask = inputs["attention_mask"]

        # Predict with the model
        with torch.no_grad():
            outputs = self.model(input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            probs = F.softmax(logits, dim=1)
            predicted_label_idx = torch.argmax(probs, dim=1).item()
        
        # Decode the predicted label
        predicted_label = label_encoder.inverse_transform([predicted_label_idx])[0]
        return predicted_label