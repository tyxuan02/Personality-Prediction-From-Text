# model_predictor.py
import torch
from transformers import BertTokenizer, BertConfig, BertModel, BertPreTrainedModel
import torch.nn as nn
from utils import preprocess_text, bert_tokenize

class Model:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', clean_up_tokenization_spaces=False)
        self.model = BertWithCustomClassifier(BertConfig.from_pretrained('bert-base-uncased', num_labels=4))
        self.model.load_state_dict(torch.load('best_model.pth', map_location=torch.device('cpu'), weights_only=True))
        self.model.eval()

    def predict(self, text):
        cleaned_text = preprocess_text(text)
        print(cleaned_text)
        print(len(cleaned_text.split()))
        input_ids, attention_mask = bert_tokenize(self.tokenizer, cleaned_text)
        with torch.no_grad():
            outputs = self.model(input_ids, attention_mask=attention_mask)
            probs = outputs[1]
        
        # Convert probabilities to binary (0 or 1) using a threshold of 0.5
        binary_predictions = (probs > 0.5).int()

        # Define the mapping for each MBTI dimension
        trait_mapping = {
            "IE": {0: "I", 1: "E"},
            "NS": {0: "N", 1: "S"},
            "TF": {0: "T", 1: "F"},
            "JP": {0: "J", 1: "P"}
        }

        # Decode the binary predictions to MBTI traits
        predicted_traits = [
            trait_mapping["IE"][binary_predictions[0][0].item()],
            trait_mapping["NS"][binary_predictions[0][1].item()],
            trait_mapping["TF"][binary_predictions[0][2].item()],
            trait_mapping["JP"][binary_predictions[0][3].item()],
        ]

        # Combine traits into MBTI type
        predicted_mbti_type = "".join(predicted_traits)

        return probs, binary_predictions, predicted_mbti_type
        
class BertWithCustomClassifier(BertPreTrainedModel):
    def __init__(self, config):
        super().__init__(config)
        self.num_labels = config.num_labels
        
        # BERT base model
        self.bert = BertModel(config)
        
        # Single linear layer for classification
        self.classifier = nn.Sequential(
            nn.Linear(config.hidden_size, config.num_labels),
            nn.Sigmoid()
        )
        
        self.init_weights()
    
    def forward(self, 
                input_ids=None, 
                attention_mask=None, 
                token_type_ids=None,
                labels=None):
        
        outputs = self.bert(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids
        )
        
        pooled_output = outputs[1]
        logits = self.classifier(pooled_output)
    
        loss = None
        if labels is not None:
            loss_fct = nn.BCELoss()
            loss = loss_fct(logits, labels.float())
            
        return loss, logits if loss is not None else logits