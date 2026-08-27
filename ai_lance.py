import json


def chat():
    print("AI-LANCE: Hello! I am AI-LANCE. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input in ["bye", "exit", "quit"]:
            print("AI-LANCE: Goodbye!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("AI-LANCE: Hello! How can I help you?")
        elif "how are you" in user_input:
            print("AI-LANCE: I am functioning perfectly. Thank you for asking!")
        elif "name" in user_input:
            print("AI-LANCE: My name is AI-LANCE.")
        else:
            print("AI-LANCE: I am still learning. Please try asking something else.")


if __name__ == "__main__":
    chat()
