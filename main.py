from assistant import ask_assistant

messages = []
choices ={
    "1":"You are a Teacher.You have to explain in such a way that any dumb can understand",
    "2":"You are a Friend.You should be helpful and supportive",
    "3":"You are a Comedian.You should make people laugh",
    "4":"You are an Interviewer. Ask me questions related to Python, one question at a time. As soon as you get an answer, give me feedback on it."
}

# Displaying the choices to the user.
print("Please choose how you want me to behave during the conversation:")
for i,chice in choices.items():
    print(f"{i}. {chice.split('.')[0]}") 

# Keeping the input loop to ensure valid choice is made .
while True:
    choice_input = input("Enter your choice (1-4): ")
    if choice_input not in choices:
        print("Please enter a number between 1 and 4.")
        continue
    else:
        break   

messages.append({"role": "system", "content": f"{choices[choice_input]},Reply in max of 100 words."})

# Greeting the user based on the choice made.
print(f"Hello! I will be your {choices[choice_input].split('.')[0].split(' ')[-1]}. I am here to help you!(Type 'exit' to quit the conversation.)")

# Main conversation loop.
while True:
    user_input = input("You: ")
    if user_input == "":
        print("Please enter a message.")
        continue
    elif user_input.lower() == "exit":
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})
    print("Thinking...", flush=True)
    answer = ask_assistant(messages)
    messages.append({"role": "assistant", "content": answer.choices[0].message.content})
    print("Assistant:", answer.choices[0].message.content)