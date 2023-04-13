import openai
from openai_pricing_logger import openai_api_listener
import config

openai.api_key = config.key

'''def test_api_call(prompt):
    model = "text-davinci-003"
    completions = openai.Completion.create(engine=model, prompt=prompt, max_tokens=7, temperature=0)
    print(completions.choices[0].text.strip())'''

def test_chat_api_call(messages):
    model = "gpt-3.5-turbo"
    completions = openai.ChatCompletion.create(model=model, messages=messages)
    print(completions.choices[0].message['content'])

if __name__ == "__main__":
    prompt = "Translate the following English text to French: 'Hello, how are you?'"
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Knock knock."},
        {"role": "assistant", "content": "Who's there?"},
        {"role": "user", "content": "Orange."},
    ]
    #messages = [{"role": "user", "content": "Translate 'Hello, how are you?' to French."}]

    with openai_api_listener():
        print("Completion Example:")
        #test_api_call(prompt)
        print("\nChatCompletion Example:")
        test_chat_api_call(messages)

