# 📧 Smart Reply System - Spam Detection with 3 ML Models

An intelligent spam detection and smart auto-reply suggestion system built with Python, Flask & Machine Learning.
Perfect for SMS, Email, and Chat message filtering.

Live Demo
bash
python app_all_models.py
Open http://127.0.0.1:5000

🤖 Models Used & Accuracy
Model	Accuracy	Use Case
Decision Tree (DT)	100%	Best for meeting / normal chat detection
Random Forest (RF)	98%	Best balanced model
Naive Bayes (NB)	95%	Best for spam / lottery messages
> All 3 models are live on the web app. User can select any model from dropdown.

> Note on Accuracy: 100% accuracy is on my small custom dataset (~100-200 messages) used for demo. 
Decision Tree shows 100% due to small data size. 
On larger real-world data, accuracy is typically 85-95%. Can be improved with more data.

✨ Features
- ✅ Spam vs Not Spam / Meeting Prediction
- 💬 Smart Reply Suggestion (Auto)
- 🔄 Model Selector - Compare 3 algorithms
- 🎯 Hybrid Logic: Rule-based (coffee, meeting, win, lottery) + ML Prediction
- 🌐 Clean Flask Web Interface
- 📱 Mobile Friendly UI

📸 Screenshots

1. Main UI - Empty
Clean homepage with input and model selector.

2. Not Spam Detection
Input: meet me for coffee | Model: Decision Tree (100%) | Result: Not Spam / Meeting

3. Spam Detection
Input: congratulations you won 100000 | Model: Naive Bayes (95%) | Result: Spam

🛠️ Installation

```bash

# Install requirements
pip install -r requirements.txt

# Run the app
python app_all_models.py