import openai

openai.API_KEY = "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"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  
        prompt=prompt,
        max_tokens=100 
    )

    return response['choices'][0]['text'].strip()

print("Welcome to the Chatbot! Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    
    chatbot_response = generate_response(user_input)
    
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": chatbot_response}
        ]
    )

    print("Chatbot:", completion['choices'][0]['message']['content'])
