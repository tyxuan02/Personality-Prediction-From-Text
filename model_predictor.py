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
            probs = F.softmax(logits, dim=1).cpu().numpy()[0]  # Convert to numpy for easier manipulation

        # Map each probability to the corresponding MBTI type
        mbti_types = label_encoder.inverse_transform(range(len(probs)))

        # Initialize trait probabilities
        trait_probabilities = {
            'I': 0, 'E': 0,
            'N': 0, 'S': 0,
            'T': 0, 'F': 0,
            'J': 0, 'P': 0
        }

        # Sum probabilities for each trait based on MBTI types
        for mbti_type, prob in zip(mbti_types, probs):
            if mbti_type[0] == 'I':
                trait_probabilities['I'] += prob
            else:
                trait_probabilities['E'] += prob
            
            if mbti_type[1] == 'N':
                trait_probabilities['N'] += prob
            else:
                trait_probabilities['S'] += prob
            
            if mbti_type[2] == 'T':
                trait_probabilities['T'] += prob
            else:
                trait_probabilities['F'] += prob
            
            if mbti_type[3] == 'J':
                trait_probabilities['J'] += prob
            else:
                trait_probabilities['P'] += prob

        # Normalize the probabilities for each trait dimension
        for dimension in ['I', 'E'], ['N', 'S'], ['T', 'F'], ['J', 'P']:
            total_prob = trait_probabilities[dimension[0]] + trait_probabilities[dimension[1]]
            trait_probabilities[dimension[0]] /= total_prob
            trait_probabilities[dimension[1]] /= total_prob

        # Find the MBTI type with the highest probability
        predicted_type_idx = probs.argmax()
        predicted_type = mbti_types[predicted_type_idx]
        predicted_type_prob = probs[predicted_type_idx]

        mbti_type_probabilities = {trait: prob for trait, prob in zip(mbti_types, probs)}

        # # Return only the predicted MBTI traits
        # trait_probabilities = {trait: prob for trait, prob in trait_probabilities.items() if trait in predicted_type}

        return predicted_type, mbti_type_probabilities # predicted_type_prob,
        