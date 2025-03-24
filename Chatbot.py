"""
This is a simple chatbot that responds to basic user inputs. Here’s a quick breakdown:

What It Does:
Greets users and responds to phrases like "hello," "how are you," "your name," "date/time," "thanks," and "weather."

Uses keyword matching (e.g., if input contains "hello", it replies with a greeting).

Tells the current date/time using datetime.

Exits when you type "quit".

Example Interactions:
You: "Hi" → Bot: "Hi there! I can help with date and time."

You: "What’s the date?" → Bot: Prints today’s date/time.

You: "Thanks!" → Bot: "You’re welcome!"

You: "Weather?" → Bot: "I don’t have weather info.
"""
import datetime
def simple_chatbot():
    print("Try to interact with me using a simple words")
    print("Hello! I'm a simple chatbot. Type quit to exit")
    
    
    while True:
        user_input = input("You: ").lower()
        
        if 'quit' in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
            
        elif 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hi there! I can help you with date and time. What do you want?")
            
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a program, but I can say I am functioning well. What about you?")
        elif "fine" in user_input or "I am fine" in user_input:
            print("That is very nice. So how can I help you?")
            
        elif 'your name' in user_input or "name" in user_input:
            print("Chatbot: I'm SimpleBot, your basic chatbot friend!")
            
        elif 'date' in user_input or "time" in user_input:
            current_date = datetime.datetime.now()
            print("Chatbot: Today's date is", current_date)
            
        elif 'thank' in user_input or "thanks" in user_input or "thank you" in user_input:
            print("Chatbot: You're welcome! Is there anything else I can help with?")
            
        elif 'weather' in user_input or "what is the weather" in user_input:
            print("Chatbot: I'm sorry, I don't have weather information. I'm a very simple bot.")
            
        else:
            print("Chatbot:I do not understand your question. Can you try asking something else? or make the question in simple words.")

simple_chatbot()