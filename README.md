# Multilingual Hate Speech Detection using MuRIL

A multilingual NLP project for detecting hate speech across:

- English
- Hindi
- Hinglish (code-mixed Hindi + English)

This project fine-tunes Google's MuRIL transformer model for binary hate speech classification and deploys it through a Django web application integrated with Hugging Face Inference API.

---

## Demo

### Web Application Features
- Input text detection
- Hate / Non-Hate prediction
- Confidence score percentage
- About page with project details
- Lightweight deployment using Hugging Face hosted model

---

## Hugging Face Model

Model hosted on Hugging Face:

**Hugging Face Repository:**  
https://huggingface.co/AadityaSinghTariyal/hate-speech-detection

---

## Problem Statement

Social media platforms contain increasing amounts of:

- abusive language
- offensive comments
- hate targeting religion/caste/community/gender

Manual moderation is expensive and slow.

This project aims to build an automated multilingual hate speech detector capable of understanding Indian language contexts.

---

## Model Used

### MuRIL
**Model:** `google/muril-base-cased`

MuRIL was selected because it is specifically designed for Indian multilingual tasks.

Advantages:
- Supports 16+ Indian languages
- Handles Devanagari well
- Performs better than standard BERT for Hindi tasks
- Good transfer learning for code-mixed text

---

## Dataset

Two datasets were experimented with.

### 1. Final Cleaned Dataset
Contains:
- cleaner labels
- corrected annotations
- language tags

Issues:
- strong class imbalance
- very few hate samples

Result:
- high accuracy but model predicted mostly class 0

---

### 2. Combined Hate Speech Dataset (Selected)

Used for final training.

Contains:
- larger data volume
- more balanced labels
- multilingual samples

Columns used:
- `text`
- `hate_label`
- `language`

Languages:
- English
- Hindi
- Hinglish

Final training dataset size: **29,550 rows**

---

## Training Pipeline

### Data Processing
- Removed null values
- Verified label consistency
- Sampled records for manual inspection
- Tokenization using MuRIL tokenizer

### Tokenization
Parameters:
- truncation=True
- max_length=256

---

## Training Strategy

Fine-tuning performed using Hugging Face Transformers with PyTorch.

### Techniques Used
- weighted loss for class imbalance
- early stopping
- lower learning rate tuning
- threshold tuning

### Hyperparameters

```python
learning_rate = 1e-5
batch_size = 16
epochs = 5
weight_decay = 0.01
max_length = 256
```

---

## Challenges Faced

### 1. Class Imbalance
Problem:
- too many class 0 samples in cleaned dataset

Effect:
- model predicted mostly non-hate

Solution:
- switched to combined dataset
- applied class weights

---

### 2. Hinglish Performance
Problem:
- Hinglish data quality was inconsistent
- spelling variations
- slang
- Romanized Hindi ambiguity

Examples:
- "tum pagal ho"
- "tm pgl ho"
- "tu pagal hai"

Effect:
- reduced generalization quality

Possible improvement:
- collect better Hinglish dataset
- normalize Hinglish spellings

---

### 3. Transformers Version Issues
Errors faced:
- Trainer tokenizer argument deprecated
- compute_loss API changes
- model loading warnings

Solution:
- updated code for latest transformers version

---

### 4. Model Size
Problem:
- MuRIL model too large for local deployment

Solution:
- uploaded model to Hugging Face
- used Inference API instead of local model loading

---

## Final Results

### Classification Report

```text
precision    recall  f1-score   support

0       0.74      0.76      0.75      3165
1       0.71      0.69      0.70      2745

accuracy                           0.73      5910
macro avg       0.73      0.72      0.73      5910
weighted avg    0.73      0.73      0.73      5910
```

### Final Accuracy
**73%**

---

## Project Architecture

```text
User Input
   ↓
Django Frontend
   ↓
Hugging Face Inference API
   ↓
Fine-tuned MuRIL Model
   ↓
Prediction Output
```

---

## Deployment Stack

### Backend
- Django

### ML Framework
- PyTorch
- Hugging Face Transformers

### Model Hosting
- Hugging Face Hub

---

## Future Improvements

### Data Improvements
- larger multilingual dataset
- better Hinglish quality
- more balanced hate examples

### Model Improvements
- XLM-Roberta comparison
- IndicBERT comparison
- ensemble models

### Explainability
- SHAP
- LIME
- attention visualization

### Production Improvements
- Docker deployment
- CI/CD
- API caching
- async inference

---

## How to Run Locally

### Clone repository

```bash
git clone YOUR_GITHUB_REPO
cd hate_speech_project
```

### Install dependencies

```bash
pip install django requests
```

### Run server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

## Sample Inputs

### Hate
```text
All xyz people are criminals
```

```text
tum log sab gande ho
```

---

### Non Hate
```text
You are amazing
```

```text
Mujhe tumhari baat pasand nahi aayi
```

---

## Key Learnings

Through this project I learned:

- transformer fine-tuning
- multilingual NLP
- handling class imbalance
- threshold tuning
- model deployment
- Hugging Face model hosting
- Django integration with ML models

---

## Author

**Aaditya Singh Tariyal**

Hugging Face:  
https://huggingface.co/AadityaSinghTariyal

---
