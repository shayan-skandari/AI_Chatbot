name = None

while True:
    user_input = input("You: ").lower()

    # ==========================
    # Exit
    # ==========================

    if user_input == "exit":
        break

    # ==========================
    # Hello Hi Hey
    # ==========================

    elif user_input in ["hello", "hi", "hey"]:
        if name is not None:
            print(f"hello {name}, how can i help you?")
        else:
            print("hello! how can i help you?")  

    # ==========================
    # Goodbye See you See ya
    # ==========================          


    elif user_input in ["bye","goodbye","see you","see ya"]:
        print("Bot: Goodbye! See you later.") 

    # ==========================
    # How are you
    # ==========================    

    elif user_input == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    # ==========================
    # Thanks Thank you Thx
    # ==========================      

    elif user_input in ["thanks","thank you","thx"]:
        print("Bot: You're welcome!")

    # ==========================
    # Good Morning
    # ==========================     

    elif user_input == "good morning":
        print("Bot: Good morning! Have a great day!")

    # ==========================
    # Good night
    # ==========================     

    elif user_input == "good night":
        print("Bot: Good night! Sleep well!")


    # ==========================
    # My name is . . . 
    # ==========================    

    elif user_input.startswith("my name is "):
        parts =  user_input.split()
        name = " ".join(parts[3:]).strip()

        print(f"Bot: Nice to meet you, {name}!")


    elif user_input == "what is my name?":
        if name is not None:

            print(f"your name is {name}!")

        else:
            print("Bot: i don't know your name yet.")    


    # ==========================
    # None
    # ==========================
        
    else:
        print("Sorry, I dont understand that yet.")

                   

