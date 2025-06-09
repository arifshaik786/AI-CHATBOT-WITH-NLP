import spacy
from spacy.matcher import PhraseMatcher

# Load English tokenizer, POS tagger, parser, NER
nlp = spacy.load("en_core_web_sm")

# Initialize PhraseMatcher
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

# Define patterns (extendable)
patterns = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "goodbye", "see you", "take care"],
    "thanks": ["thanks", "thank you", "much appreciated"],
    "help": ["help", "can you help me", "i need support"],
    "name": ["what is your name", "who are you"],
    "age": ["how old are you", "your age"]
}

# Add patterns to matcher
for label, phrases in patterns.items():
    matcher.add(label, [nlp(text) for text in phrases])

# Response dictionary
responses = {
    "greeting": "Hello! How can I assist you today?",
    "goodbye": "Goodbye! Have a nice day!",
    "thanks": "You're welcome!",
    "help": "Sure, I'm here to help. What do you need assistance with?",
    "name": "I'm a simple AI chatbot created using spaCy.",
    "age": "I'm timeless! I'm just a script after all."
}

def chatbot_response(user_input):
    doc = nlp(user_input)
    matches = matcher(doc)
    if matches:
        match_id, start, end = matches[0]
        response_key = nlp.vocab.strings[match_id]
        return responses.get(response_key)
    else:
        return "I'm sorry, I didn't understand that. Can you rephrase?"

# Main Chatbot Loop
if __name__ == "__main__":
    print("Chatbot: Hello! I’m your NLP assistant. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot:", responses["goodbye"])
            break
        print("Chatbot:", chatbot_response(user_input))
