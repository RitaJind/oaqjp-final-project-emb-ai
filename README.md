# 🧠 AI-Powered Emotion Detection - Web Application

A **modern web application** built with Flask and Watson NLP that analyzes text to detect and classify human emotions with real-time sentiment analysis capabilities.

![Flask](https://img.shields.io/badge/Flask-2.0+-red.svg)
![Python](https://img.shields.io/badge/Python-3.9+-yellow.svg)
![Watson](https://img.shields.io/badge/Watson-NLP-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-4.3+-purple.svg)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-orange.svg)
![HTML5](https://img.shields.io/badge/HTML5-5.0+-red.svg)

## 🚀 Project Overview

AI-powered emotion detection web application that leverages IBM Watson's Natural Language Processing to analyze text and identify emotional sentiment. Users can input any text and receive detailed emotion scores across five key emotional categories with dominant emotion identification.

**Key Technologies:** Flask | Watson NLP | JavaScript | Bootstrap | Python

## 📋 Features

**Core Functionality:**
- 🎯 **Emotion Analysis** - Detects 5 emotions: anger, disgust, fear, joy, and sadness
- 🧠 **AI-Powered** - Uses IBM Watson NLP emotion analysis service
- 📊 **Detailed Scoring** - Provides numerical scores for each emotion category
- 🎪 **Dominant Emotion** - Identifies the strongest emotional signal in text
- 📱 **Responsive Design** - Mobile-optimized interface with Bootstrap styling
- ⚡ **Real-time Analysis** - Instant emotion detection via AJAX requests

## 🏃‍♂️ Quick Start

**Prerequisites:** Python 3.9+, Internet connection for Watson API

```bash
# Clone repository
git clone https://github.com/RitaJind/oaqjp-final-project-emb-ai.git
cd oaqjp-final-project-emb-ai

# Install dependencies
pip install flask requests

# Start the application
python server.py
```

**Access Application:** http://localhost:5000

## 🔄 Application Flow

**User Journey:** Homepage → Text Input → Click "Run Sentiment Analysis" → View Emotion Scores → Analyze Results

**Sample Analysis:**
- Input: "I am so excited about this new opportunity!"
- Output: Joy: 0.9, Anger: 0.1, Fear: 0.0, Disgust: 0.0, Sadness: 0.0
- Dominant Emotion: Joy

## 🏗️ Architecture

**Application Stack:** Frontend (HTML/JS/Bootstrap) ↔ Flask Server ↔ Watson NLP API

**Tech Stack:** Flask 2.0+ | Python 3.9+ | Watson NLP | Bootstrap 4.3+ | JavaScript ES6+

## 📡 API Documentation

**Key Endpoints:**
- `GET /` - Renders the main application interface
- `GET /emotionDetector?textToAnalyze={text}` - Analyzes emotions in provided text

**Response Format:**
```json
{
  "anger": 0.1,
  "disgust": 0.0,
  "fear": 0.0,
  "joy": 0.9,
  "sadness": 0.0,
  "dominant_emotion": "joy"
}
```

## 🧪 Testing

```bash
# Run unit tests
python test_emotion_detection.py

# Test API endpoint
curl "http://localhost:5000/emotionDetector?textToAnalyze=I am happy today"

# Sample test cases included:
# - Joy detection: "I am glad this happened"
# - Anger detection: "I am really mad about this"
# - Fear detection: "I am really afraid that this will happen"
# - Sadness detection: "I am so sad about this"
# - Disgust detection: "I feel disgusted just hearing about this"
```

## 📁 Project Structure

```
oaqjp-final-project-emb-ai/
├── server.py                    # Flask application server
├── test_emotion_detection.py    # Unit tests for emotion detection
├── EmotionDetection/
│   ├── __init__.py             # Package initialization
│   └── emotion_detection.py    # Core emotion analysis logic
├── templates/
│   └── index.html              # Main web interface
├── static/
│   └── mywebscript.js          # Client-side JavaScript
└── README.md                   # Project documentation
```


## 👨‍💻 About the Developer

**Rita Jindal** - AI/ML Developer  

*Passionate about building intelligent applications that leverage natural language processing and machine learning. Experienced in Python ecosystem, web development, and AI integration for practical solutions.*
