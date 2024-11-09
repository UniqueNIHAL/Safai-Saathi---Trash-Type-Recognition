import os
import requests

API_ENDPOINT = 'https://api.gemini-ai.com/v1/chat/completions'
API_KEY = os.getenv('GEMINI_API_KEY')  # Store your API key as an environment variable

system_prompt = '''
You are an expert assistant on the Trash Recognition Project, which aims to revolutionize waste management by using technology to recognize and categorize trash. You also provide information on waste segregation, its importance, best practices, and its alignment with global initiatives like the UN Sustainable Development Goals and the Swachh Bharat Mission.
'''

conversation = [
    {'role': 'system', 'content': system_prompt}
]

def get_chatbot_response(conversation):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    
    data = {
        'model': 'gemini-chat-model',
        'messages': conversation
    }
    
    try:
        response = requests.post(API_ENDPOINT, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.RequestException as err:
        print("Error: ", err)
    return None

# Conversational loop
print("Welcome to the Trash Recognition Project Chatbot! Type 'exit' to end the conversation.")
while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Thank you for chatting! Goodbye!")
        break
    conversation.append({'role': 'user', 'content': user_input})
    chatbot_response = get_chatbot_response(conversation)
    if chatbot_response:
        print(f"Chatbot: {chatbot_response}")
        conversation.append({'role': 'assistant', 'content': chatbot_response})
    else:
        print("Chatbot: I'm sorry, but I'm unable to process your request at the moment.")
