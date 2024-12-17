import openai

# Add your OpenAI API key here
openai.api_key = "your-openai-api-key"

def chat_with_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    user_input = input("Ask me anything: ")
    print(chat_with_openai(user_input))
