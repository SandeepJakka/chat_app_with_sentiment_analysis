from transformers import pipeline
import random

sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

response_templates = {
    "positive": [
        "Awesome! Keep up the positivity! 💪",
        "That's fantastic to hear! 🌟",
        "I'm here to cheer you on! 🎉",
        "Keep going, you're doing great! 🙌",
        "That's amazing! Keep shining! ✨",
        "Your positivity is contagious! 😊",
        "I'm so happy to hear that! 🌈",
        "You're on the right path—keep it up! 🚀",
        "Sounds wonderful! I’m cheering for you! 👏",
        "Such great energy! Tell me more! 🌟",
        "I'm glad things are going so well! 😄",
    ],
    "negative": [
        "Sending some positive vibes your way! 🌈",
        "I understand—things can be tough sometimes. 💙",
        "I'm here for you, take it easy. 💜",
        "Don't worry, things will get better soon. 💫",
        "I'm here for you, hang in there. 💪",
        "It’s okay to have tough days. Take your time. 🌱",
        "Remember, every day is a new chance to start fresh. 🌄",
        "You're not alone—I'm here to chat anytime. 🫂",
        "It’s completely natural to feel this way. Take care. 🌼",
        "Sending you strength and good thoughts. 🌻",
        "Let me know if there's anything I can do to help. 💚"
    ],
    "neutral": [
        "I’m listening, go on!",
        "Let's keep the conversation going. 😊",
        "I'm here if you want to chat.",
        "Tell me more about that!",
        "Got it! What else is on your mind? 🤔",
        "I’m here to listen—tell me more. 😊",
        "That sounds interesting! Keep going.",
        "I'm all ears. What's next? 👂",
        "I'm here whenever you're ready to share more.",
        "Thanks for sharing! What’s on your mind next?",
        "I'm here and listening carefully. Let’s chat!"
    ]
}



def analyze_sentiment(message):
    
    result = sentiment_pipeline(message)
   
    print(f"Full model output: {result}")
    
    prediction = result[0]
    label = prediction['label']
    confidence = prediction['score']
    
    if label == 'LABEL_0':  
        sentiment = 'negative'
    elif label == 'LABEL_1':  
        sentiment = 'neutral'
    elif label == 'LABEL_2':  
        sentiment = 'positive'
    else:
        sentiment = 'neutral'  
    
    print(f"Sentiment: {sentiment}, Confidence: {confidence}")

    if sentiment == 'positive':
        response = random.choice(response_templates["positive"])
    elif sentiment == 'negative':
        response = random.choice(response_templates["negative"])
    else:
        response = random.choice(response_templates["neutral"])
    
    return response, sentiment

