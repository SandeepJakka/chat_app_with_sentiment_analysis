
function addMessageToChat(message, sender) {
    const chatContainer = document.querySelector('.chat-container');
    const messageElement = document.createElement('div');
    
    if (sender === 'user') {
        messageElement.classList.add('user-message', 'message');
    } else {
        messageElement.classList.add('bot-message', 'message');
    }
  
    const convertedMessage = convertEmoticons(message);
    messageElement.innerHTML = convertedMessage; 
    
    chatContainer.appendChild(messageElement);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function convertEmoticons(text) {
    const emoticonMapping = {
        ':)': '😊',
        ':D': '😁',
        ':(': '☹️',
        ';)': '😉',
    };
 
    return text.replace(/(:\)|:D|:\(|;))/g, match => emoticonMapping[match] || match);
}

function handleUserMessage() {
    const userMessage = document.getElementById('user-input').value;
    if (userMessage === '') {
        alert('Please enter a message.');
        return;
    }

    addMessageToChat(userMessage, 'user');
    
    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: userMessage }),
    })
    .then(response => response.json())
    .then(data => {
        const botResponse = getBotResponse(data.sentiment);
        addMessageToChat(botResponse, 'bot');
    })
    .catch(error => console.error('Error:', error));
}

function getBotResponse(sentiment) {
    const responses = {
        positive: [
            "That's awesome! Keep shining! 🌟",
            "Great to hear! You're doing amazing! 💪",
            "You're killing it! Keep going! 🎉"
        ],
        negative: [
            "I'm here for you. Things will get better. 💙",
            "I understand—sometimes it's tough. 😌",
            "Sending some positive vibes your way! 🌈"
        ],
        neutral: [
            "Okay, sounds good! Let me know if you want to talk more. 😊",
            "Got it! What's on your mind? 🤔",
            "I'm here to listen whenever you need. 😌"
        ]
    };

    if (sentiment === 'positive') {
        return responses.positive[Math.floor(Math.random() * responses.positive.length)];
    } else if (sentiment === 'negative') {
        return responses.negative[Math.floor(Math.random() * responses.negative.length)];
    } else {
        return responses.neutral[Math.floor(Math.random() * responses.neutral.length)];
    }
}
