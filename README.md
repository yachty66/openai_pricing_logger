# openai_pricing_logger 

openai_pricing_logger is a Python package that logs OpenAI API costs and timestamps. It's designed to help you keep track of API usage and related costs, providing an easy way to monitor and analyze the expenses.

## Features

- Automatically logs API call costs and timestamps
- Easy integration with OpenAI's GPT-3.5-turbo and GPT-4 models
- Lightweight and easy to use

## Installation

To install openai_pricing_logger, run the following command in your terminal:

```bash
pip install openai_pricing_logger 
```

## Usage 

1. Import the openai_api_listener context manager from the logger_package:

```python
from logger_package import openai_api_listener
```

2. Wrap your OpenAI API calls with the openai_api_listener context manager:

```python
import openai

with openai_api_listener():
    # Your OpenAI API calls go here
```

3. The package will automatically log the cost and timestamp of each API call to a file named api_calls.log in the current directory.

## Contributing

Contributions are welcome! Please feel free to open issues and submit pull requests on the [GitHub repository](https://github.com/yachty66/openai_pricing_logger).

## License

openai_pricing_logger is licensed under the [MIT License](LICENSE).


