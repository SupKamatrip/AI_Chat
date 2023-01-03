import openai

# Set the API key
openai.api_key = "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"

# Define the model to use
model_engine = "text-davinci-002"

# Set the prompt for the chatbot
prompt = input(" Quel est votre question ? ")

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the response
message = completion.choices[0].text
print(message)
