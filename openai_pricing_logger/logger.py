import contextlib
import functools
import json
import openai
import time
import os

def load_pricing():
    # Get the current script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the pricing.json file within the package
    pricing_path = os.path.join(script_dir, "pricing.json")

    with open(pricing_path) as f:
        return json.load(f)

PRICING = load_pricing()

def get_rate_per_token(model, prompt_tokens, completion_tokens):
    if model == "gpt-3.5-turbo":
        usage = PRICING[model]["usage"]
        tokens = prompt_tokens + completion_tokens
        cost = (usage / 1000) * tokens
        return cost
    elif model == "gpt-4":
        prompt = PRICING[model]["prompt"]
        cost_prompt = (prompt / 1000) * prompt_tokens
        completion = PRICING[model]["completion"]
        cost_completion = (completion / 1000) * completion_tokens
        cost = cost_prompt + cost_completion
        return cost 
    #TODO add support for other models

def log_cost_and_timestamp(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        model = kwargs.get("model", "unknown")
        response = func(*args, **kwargs)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        cost = get_rate_per_token(model, response["usage"]["prompt_tokens"], response["usage"]['completion_tokens'])
        cost_float = float(cost)
        cost_str = f"{cost_float:.10f}" 
        cost_formatted = cost_str.rstrip('0').rstrip('.')
        print(cost_formatted)
        log_file = 'api_calls.log'
        if not os.path.exists(log_file):
            with open(log_file, 'w') as f:
                f.write('')
        with open(log_file, 'r') as f:
            total_cost = 0
            for line in f:
                entry = json.loads(line)
                total_cost += float(entry['cost'])
        total_cost += cost_float
        total_cost_str = f"{total_cost:.10f}"
        total_cost_formatted = total_cost_str.rstrip('0').rstrip('.')
        with open(log_file, 'a') as f:
            log_entry = {
                'timestamp': timestamp,
                'model': model,
                'cost': cost_formatted,
                'total_cost': total_cost_formatted,
            }
            f.write(json.dumps(log_entry) + '\n')
        return response
    return wrapper
        
@contextlib.contextmanager
def openai_api_listener():
    original_create = openai.Completion.create
    openai.Completion.create = log_cost_and_timestamp(original_create)
    original_chat_create = openai.ChatCompletion.create
    openai.ChatCompletion.create = log_cost_and_timestamp(original_chat_create)
    try:
        yield
    finally:
        openai.Completion.create = original_create
        openai.ChatCompletion.create = original_chat_create
