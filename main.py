from assistant import ask_assistant

messages = []
while True:
    user_input = input("You: ")
    if user_input == "":
        print("Please enter a message.")
        continue
    elif user_input.lower() == "exit":
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})
    print("Searching...", flush=True)
    answer = ask_assistant(messages)
    messages.append({"role": "assistant", "content": answer.choices[0].message.content})
    print("Assistant:", answer.choices[0].message.content)