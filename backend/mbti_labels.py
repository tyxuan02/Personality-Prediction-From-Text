import numpy as np
from sklearn.preprocessing import LabelEncoder

labels = np.array(['ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'ESTP',
       'INFJ', 'INFP', 'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP'], dtype=object)

# Label each type of MBTI
label_encoder = LabelEncoder()
label_encoder.fit_transform(labels) 