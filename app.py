from flask import Flask, render_template, request, jsonify
from sentiment_analysis import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
  
    user_message = request.form['message']

    if not user_message:
        return jsonify({"error": "Please enter a message."})

    response, sentiment = analyze_sentiment(user_message)
    
    return jsonify({"response": response, "sentiment": sentiment})

if __name__ == '__main__':
    app.run(debug=True)
