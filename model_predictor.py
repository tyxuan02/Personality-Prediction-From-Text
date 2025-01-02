import torch
from transformers import BertTokenizer, BertForSequenceClassification
from utils import preprocess_text, bert_tokenize
from huggingface_hub import hf_hub_download

class Model:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', clean_up_tokenization_spaces=False)
        self.model = BertForSequenceClassification.from_pretrained(
            "bert-base-uncased",
            num_labels=4,
            output_attentions=False,
            output_hidden_states=False,
            hidden_dropout_prob=0.5
        )
        model_path = hf_hub_download(repo_id="Xuan5251/mbti_personality_prediction", filename="mbti_model.pth")
        self.model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu'), weights_only=True))
        self.model.eval()

    def predict(self, text):
        cleaned_text = preprocess_text(text)
        input_ids, attention_mask = bert_tokenize(self.tokenizer, cleaned_text)
        with torch.no_grad():
            outputs = self.model(input_ids, attention_mask)

        logits = outputs.logits
        probs = torch.sigmoid(logits)
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