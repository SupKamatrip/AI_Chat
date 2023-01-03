#! /usr/bin/python3
import openai

# Set the API key
openai.api_key = "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"

# Define the model to use
model_engine = "text-davinci-003"

print("Bienvenue dans le chatbot ChatGPT. Posez-moi une question ou tapez 'exit' pour quitter.")

while True:
    # Get the user's message
    message = input("Vous : ")

    # Check if the user wants to exit
    if message.lower() == "exit":
        break

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Print the response
    response = completion.choices[0].text
    print("ChatGPT : " + response)

print("Au revoir!")
