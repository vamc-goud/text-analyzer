
# Text Analyzer

A Python command-line application that analyzes text and provides useful statistics, including word counts, character counts, sentence counts, word frequency, and average word length.

## Features

- Count words while ignoring punctuation
- Count characters, including spaces and punctuation
- Count sentences
- Calculate average word length
- Display word frequency
- Find the most frequent word
- Calculate word frequency percentages
- Identify the longest and shortest words
- Handle empty input
- Include unit tests using Python's unittest framework

## Project Structure

text_analyzer/
├── main.py
├── text_utils.py
├── test_text_utils.py
├── README.md
├── requirements.txt
└── .gitignore

## Requirements

- Python 3.10 or later
- No external packages required for the core application

## Run the Application

Clone the repository:

    git clone https://github.com/vamc-goud/text-analyzer.git

Navigate to the project directory:

    cd text-analyzer

Run the application:

    python main.py

## Run Unit Tests

    python -m unittest -v

## Example

Input:

    Python is easy. Python is powerful!

The application displays statistics such as word count, character count, sentence count, word frequency, and average word length.

## Skills Demonstrated

- Python functions and modules
- String processing
- Dictionaries and lists
- Regular expressions
- Input validation
- Unit testing
- Git and GitHub
