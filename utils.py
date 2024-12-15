from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
import re
import contractions

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('punkt_tab')

def bert_tokenize(tokenizer, text):
    encoded_input = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=128,
        padding='max_length',
        return_attention_mask=True,
        truncation=True,
        return_tensors='pt'
    )
    input_ids = encoded_input['input_ids']
    attention_mask = encoded_input['attention_mask']

    return input_ids, attention_mask

def preprocess_text(text):
    # Convert text into lower case
    text = text.lower()

    # Expand contractions
    text = contractions.fix(text)

    # Remove HTML tags
    text = re.sub(r'<.*?>', ' ', text)

    # Remove URL
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    # Remove emojis
    emoji_pattern = re.compile("["
    u"\U0001F600-\U0001F64F"  # emoticons
    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
    u"\U0001F680-\U0001F6FF"  # transport & map symbols
    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                        "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)

    # Remove digits
    text = re.sub(r'\d+', ' ', text)

    # Remove emails
    text = re.sub(r'\S+@\S+', '', text)

    # Remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)

    # Remove extra whitespaces
    text = " ".join(text.split())

    # return text

    # Tokenization
    text = word_tokenize(text)

    # Lemmatize the text using WordNetn
    lemmatizer = WordNetLemmatizer()

    # Remove stopwords
    stopwords = english_stopwords()
    words = [lemmatizer.lemmatize(word) for word in text if word not in stopwords]

    return " ".join(words)

def english_stopwords():
    english_stopwords = stopwords.words('english')
    english_stopwords = [word for word in english_stopwords]

    return english_stopwords