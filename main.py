import requests

api_endpoint = 'https://api.openai.com/v1/chat/completions'
api_key = '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'

def prompt_user_for_data():
    prompts = []
    while True:
        prompt_text = input("Enter the prompt text (or type 'exit' to stop): ")
        if prompt_text.lower() == 'exit':
            break
        filename = input("Enter the filename to save the response: ")
        prompts.append({'prompt': prompt_text, 'filename': filename})
    return prompts

def generate_chat_gpt_responses(prompts):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }

    for prompt in prompts:
        print(prompt['prompt'])
        body = {
            'model': 'gpt-3.5-turbo',
            'messages': [
                {
                    'role': 'user',
                    'content': prompt['prompt'],
                },
            ],
            'max_tokens': 3000,
            'temperature': 0.2,
        }

        response = requests.post(api_endpoint, json=body, headers=headers)
        generated_text = response.json()['choices'][0]['message']['content']

        with open(prompt['filename'], 'w', encoding='utf-8') as file:
            file.write(generated_text)

        print(f'CSV file "{prompt["filename"]}" generated successfully.')

if __name__ == "__main__":
    user_prompts = prompt_user_for_data()
    generate_chat_gpt_responses(user_prompts)
