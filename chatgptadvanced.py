#! /usr/bin/python3
import openai

# Set the API key
openai.api_key = ""

# Define the model to use
model_engine = "text-davinci-003"

print("Bienvenue dans le chatbot ChatGPT. Posez-moi une question ou tapez 'exit' pour quitter.")

while True:
    # Récupère le message de l'utilisateur
    message = input("Vous : ")

    # Regarde si l'utilisateur veut quitter le chat
    if message.lower() == "exit":
        break

    # Génère la réponse
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=message,
        max_tokens=3900,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Retourne la réponse
    response = completion.choices[0].text
    print("ChatGPT : " + response)

print("Au revoir!")
