from setuptools import setup, find_packages

setup(
    name="openai_pricing_logger",
    version="0.1",
    author="Max Hager",
    author_email="maxhager28@gmail.com",
    description="A package to log OpenAI API costs",
    url="https://github.com/yachty66/openai_pricing_logger",
    packages=find_packages(),
    package_data={"logger_package": ["pricing.json"]},
    include_package_data=True,
)
