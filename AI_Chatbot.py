while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        break

    elif user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif user_input in ["bye","goodbye","see you","see ya"]:
        print("Bot: Goodbye! See you later.") 

    elif user_input == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user_input in ["thanks","thank you","thx"]:
        print("Bot: You're welcome!")

    elif user_input == "good morning":
        print("Bot: Good morning! Have a great day!")

    elif user_input == "good night":
        print("Bot: Good night! Sleep well!")            

    else:
        print("Sorry, I dont understand that yet.")

                   

