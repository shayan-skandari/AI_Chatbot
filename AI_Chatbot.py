name = None

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        break

    elif user_input in ["hello", "hi", "hey"]:
        if name is not None:
            print(f"hello {name}, how can i help you?")
        else:
            print("hello! how can i help you?")    


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

    elif user_input.startswith("my name is "):
        name = user_input.replace("my name is", "")
        print(f"Bot: Nice to meet you, {name}!")

    elif user_input == "what is my name?":
        if name is not None:

            print(f"your name is {name}!")

        else:
            print("Bot: i don't know your name yet.")    

        
    else:
        print("Sorry, I dont understand that yet.")

                   

