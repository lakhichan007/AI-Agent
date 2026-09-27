from assistant import ask_assistant


while True:
    user_input = input("You: ")
    if user_input == "":
        print("Please enter a message.")
        continue
    elif user_input.lower() == "exit":
        print("Goodbye!")
        break

    answer = ask_assistant(user_input)
    print("Assistant:", answer.choices[0].message.content)