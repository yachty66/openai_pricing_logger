# openai_api_price_calculator

## Tasks
- [x] add real prices
- [x] get number of tokens from response
- [x] define which data should be visible inside the logs 
- [x] add column in logs for total
- [x] test if logs work for several messages in the stack
- [x] convert total costs to something readable 

- [x] test with python package conditions 

- [ ] try to create a python package for it and push it to python packages

- [ ] check if it works as expected   


- https://openai.deepakness.com/ --> only provides information about 

## Last steps
- [ ] make a cool logo and explain ideas about contributions
    - [ ] support for all other models and also dalle?
    - [ ] send denmark guy have him on twitter?

## Notes 

Model	Prompt	Completion
8K context	$0.03 / 1K tokens	$0.06 / 1K tokens
32K context	$0.06 / 1K tokens	$0.12 / 1K tokens

Model	Usage
gpt-3.5-turbo	$0.002 / 1K tokens

which infos should th e

I need to get all the possible ways of how can request is made. I want to support chat and completions.

Completions only support for the most used completion model:

import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Completion.create(
  model="text-davinci-003",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)

Chat for gpt-3.5-turbo and gpt-4 

import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)

Thats what the library will support. lets finalize this project today

cool, this works. now i should be able to add the functionality of adding costs to my function. 

The 

## Goal

The goal is to create a opensource library for that. Everytime a response is made the response is saved with a timestamp in a log file. If the user wants to see the current price of the log file he can do this with running something like python whatever.. and than the price gets displayed in dollar. As soon the user made a pip install from the app if he than is running the first time a request to open ai a log file gets created automatically and in this log file every time a request is made the user can see a new entry with timestamp and cost. 

Now my question how can i observe api calls to openai?


Open ai has an api for calling their language models. every time a request is made based on the input prompt something is returned. this is costing something. i want to create a python library which is everytime a request is send to this api the cost of the request is calculated and than an entry is added to a log file additionally with an timestamp. Is that possible? 

I want to create a python library which is 

In the end I want a semi attractive interface with two input fields and a calculate button. If the calculate button is pushed a loading button appears and the price gets calculated. 

I first need to checkout tiktoken. 

I will only support gpt-4, gpt-3.5-turbo and thats it. Would be quite cool to create an open source python library for getting to know the cost. basically in the moment you make a call to the api from openai what will happen is that. 

- [ ] make a test for how that