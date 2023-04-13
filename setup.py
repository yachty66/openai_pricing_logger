from setuptools import setup, find_packages

setup(
    name="openai_pricing_logger",
    version="0.0.1",
    author="Max Hager",
    author_email="maxhager28@gmail.com",
    description="A package to log OpenAI API costs",
    url="https://github.com/yachty66/openai_pricing_logger",
    packages=find_packages(),
    package_data={"logger_package": ["pricing.json"]},
    include_package_data=True,
     classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires='>=3.6',
)
