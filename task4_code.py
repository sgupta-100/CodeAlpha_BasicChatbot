def chatbot():

    print("You are about to talk to the chatbot!! Only ask these simple questions - ")
    print("1. hello\n2. how are you?\n3. what are your features?\n4. are you strong and intelligent?\n5. Say bye if you want to exit the bot\n")

    print("Hello! I am a simple chatbot. You can talk to me. Type 'bye' to exit.\n")
   
    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "hello":
            print("Chatbot: Hi!")

        elif user_input == "how are you?":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "what are your features?":
            print("Chatbot: I can talk to you with simple commands.")

        elif user_input == "are you strong and intelligent?":
            print("Chatbot: I am a chatbot, I cannot say myself strong but I am intelligent")    

        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break  
        
        else:
            print("Chatbot: I am sorry, I do not understand that.")
# Run the chatbot
chatbot()