# Importing neccessary libraries and functions
import torch
from torch.nn import functional as F
from preprocessing import preprocess_text, bert_tokenize
from mbti_labels import label_encoder

def make_prediction(model, tokenizer, text):
    cleaned_text = preprocess_text(text)
    input_ids, attention_mask = bert_tokenize(tokenizer, cleaned_text)

    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)
        logits = outputs.logits

    probs = F.softmax(logits, dim=1)  # Converts logits to probabilities
    predicted_label_idx = torch.argmax(probs, dim=1)[0]
    predicted_label = label_encoder.inverse_transform([predicted_label_idx])[0]
    return predicted_label

# sample_text = "2024 start bang everyones yearend summary brilliant compared feel like havent lived contrast feel year younger today class realized lost red pen remembered python exam teacher borrowed yesterday didnt return realized exam there mode calculator calculate variance one click asked classmate knew said calculator allowed shanghai college entrance exam learned quite earlyduring trial clearly stated trump never involved epstein island im surprised didnt fabricate million page document drag trump im devastatedmariah carey really discerning eye time shot music video song lowbudget nobody care special effect indeed song remained popular"
# cleaned_text = preprocess_text(sample_text)
# print("Cleaned text:", cleaned_text)

# model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=len(label_encoder.classes_))
# model.load_state_dict(torch.load("bert_model.pth", map_location=torch.device('cpu')))
# model.eval()

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model.to(device)

# input_ids, attention_mask = bert_tokenize(cleaned_text)

# with torch.no_grad():
#     outputs = model(input_ids, attention_mask=attention_mask)
#     logits = outputs.logits

# probs = F.softmax(logits, dim=1)  # Converts logits to probabilities
# predicted_label_idx = torch.argmax(probs, dim=1)[0]
# predicted_label = label_encoder.inverse_transform([predicted_label_idx])[0]
# print("Predicted MBTI Type:", predicted_label)

