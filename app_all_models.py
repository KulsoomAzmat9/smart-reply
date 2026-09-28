from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

with open('spam_model_dt.pkl', 'rb') as f: dt_model = pickle.load(f)
with open('vectorizer_dt.pkl', 'rb') as f: dt_vectorizer = pickle.load(f)
with open('spam_model_nb.pkl', 'rb') as f: nb_model = pickle.load(f)
with open('vectorizer_nb.pkl', 'rb') as f: nb_vectorizer = pickle.load(f)
with open('spam_model_rf.pkl', 'rb') as f: rf_model = pickle.load(f)
with open('vectorizer_rf.pkl', 'rb') as f: rf_vectorizer = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    reply = None
    model_used = None
    message = ""
    model_choice = "rf"

    if request.method == 'POST':
        message = request.form.get('message', '')
        model_choice = request.form.get('model', 'rf')
        msg_lower = message.lower()

        if model_choice == 'dt':
            model_used = "Decision Tree (100% Accuracy)"
            vec = dt_vectorizer.transform([message])
            raw = str(dt_model.predict(vec)[0]).lower()
        elif model_choice == 'nb':
            model_used = "Naive Bayes (95% Accuracy)"
            vec = nb_vectorizer.transform([message])
            raw = str(nb_model.predict(vec)[0]).lower()
        else:
            model_used = "Random Forest (98% Accuracy)"
            vec = rf_vectorizer.transform([message])
            raw = str(rf_model.predict(vec)[0]).lower()

        MEETING_WORDS = ["coffee", "meet", "meeting", "lunch", "dinner", "tea"]
        SPAM_WORDS = ["win", "won", "lottery", "prize", "congratulation", "congratulations", "lakh", "rupees", "million", "reward", "claim"]

        if any(w in msg_lower for w in MEETING_WORDS):
            prediction = "Not Spam / Meeting"
            reply = "Sure, I can join. Please share the time and location."
        elif any(w in msg_lower for w in SPAM_WORDS):
            prediction = "Spam"
            reply = "This looks like spam, no reply needed."
        else:
            if raw == "spam" or raw == "1":
                prediction = "Spam"
                reply = "This looks like spam, no reply needed."
            else:
                prediction = "Not Spam / Meeting"
                reply = "Sure, I can join. Please share the time and location."

    return render_template('index.html', prediction=prediction, reply=reply, model_used=model_used, message=message, model_choice=model_choice)

if __name__ == '__main__':
    app.run(debug=True)