import re
import random
import datetime
from collections import defaultdict, Counter

class AdvancedChatbot:
    def __init__(self):
        self.conversation_history = []
        self.user_preferences = {}
        self.learning_data = defaultdict(list)
        self.session_start = datetime.datetime.now()
        self.user_name = None
        self.mood_indicators = {
            'positive': ['good','great','awesome','excellent','wonderful','fantastic','happy','excited'],
            'negative': ['bad','terrible','awful','sad','angry','frustrated','upset','disappointed'],
            'neutral': ['okay','fine','alright','normal','average']}
        self.knowledge_base = {
            'greetings': (['hello','hi','hey','greetings','good morning'], ['Hello! How can I assist you today?','Hi there! What is on your mind?','Greetings! I am here to help.']),
            'identity': (['who are you','what are you','your name','who made you'], ['I am an Advanced AI Assistant created by LANCE.','I am your AI companion, designed to assist and engage in meaningful conversations.']),
            'programming': (['programming','coding','python','javascript','java','c++','html','css'], ['I would be happy to help with programming! What language or concept would you like to discuss?','Programming is fascinating! Are you working on a specific project?']),
            'goodbye': (['goodbye','bye','see you','farewell','exit','quit'], ['Goodbye! It was great talking with you.','Take care! I have enjoyed our conversation.'])}

    def preprocess_text(self, text):
        text = re.sub(r'\s+', ' ', text.lower().strip())
        return text

    def analyze_sentiment(self, text):
        words = text.lower().split()
        positive = sum(w in self.mood_indicators['positive'] for w in words)
        negative = sum(w in self.mood_indicators['negative'] for w in words)
        return 'positive' if positive > negative else 'negative' if negative > positive else 'neutral'

    def calculate_similarity(self, text1, text2):
        a, b = set(text1.split()), set(text2.split())
        return len(a & b) / len(a | b) if a | b else 0

    def find_best_response(self, user_input):
        text = self.preprocess_text(user_input)
        best_category, best_score = None, 0
        for category, (patterns, _) in self.knowledge_base.items():
            for pattern in patterns:
                score = self.calculate_similarity(text, pattern)
                if score > best_score:
                    best_category, best_score = category, score
        return best_category, best_score

    def generate_contextual_response(self, user_input):
        if re.search(r'\bmy name is (\w+)', user_input.lower()):
            self.user_name = re.search(r'\bmy name is (\w+)', user_input.lower()).group(1).capitalize()
        category, confidence = self.find_best_response(user_input)
        sentiment = self.analyze_sentiment(user_input)
        if not category or confidence < 0.1:
            if any(w in user_input.lower() for w in ['time','date','today']):
                now = datetime.datetime.now()
                return f"The current time is {now.strftime('%H:%M')} and today's date is {now.strftime('%Y-%m-%d')}."
            if sentiment == 'negative':
                return 'I sense you might be feeling down. Is there something I can help you with?'
            if sentiment == 'positive':
                return 'That is great to hear! What is making you feel so good today?'
            return random.choice(['That is interesting! Can you tell me more?','I am still learning about that. Could you explain more?'])
        response = random.choice(self.knowledge_base[category][1])
        if self.user_name and category == 'greetings':
            response = f"Hello {self.user_name}! " + response
        self.learning_data[category].append(self.preprocess_text(user_input))
        return response

    def get_conversation_stats(self):
        sentiments = Counter(x['sentiment'] for x in self.conversation_history)
        return {'total_messages': len(self.conversation_history), 'dominant_sentiment': sentiments.most_common(1)[0][0] if sentiments else 'neutral', 'user_name': self.user_name}

    def chat(self, user_input):
        if user_input.lower() in ['stats','statistics','show stats']:
            s = self.get_conversation_stats()
            return f"Messages: {s['total_messages']} | Mood: {s['dominant_sentiment']}"
        response = self.generate_contextual_response(user_input)
        self.conversation_history.append({'timestamp': datetime.datetime.now(), 'user_input': user_input, 'bot_response': response, 'sentiment': self.analyze_sentiment(user_input)})
        return response

if __name__ == '__main__':
    bot = AdvancedChatbot()
    print('Advanced AI Chatbot v2.0 — type goodbye to exit')
    while True:
        user_input = input('You: ').strip()
        if user_input.lower() in ['goodbye','bye','exit','quit']:
            print('AI:', bot.chat(user_input)); break
        if user_input:
            print('AI:', bot.chat(user_input))
