while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        break

    elif user_input == "hello":
        print("Bot: Hello! How can I help you?")

    elif user_input == "bye":
        print("Bot: Goodbye! See you later.") 

    elif user_input == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    else:
        print("Sorry, I dont understand that yet.")           

