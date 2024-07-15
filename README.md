# Langflow Hackathon: Multi-language Support Application

This application is based on the technique presented at the Linux Foundation's Open Source Summit: "Translation Augmented Generation" by Raghavan Muthuregunathan.

Link: [LF AI Summit](https://sched.co/1aBOj)

## Introduction

This project was developed for the Langflow Hackathon using OpenAI and Streamlit. It allows users to ask questions or describe images in several low-resource languages and get responses in the selected language or generate images based on the descriptions.

### What is a Low-Resource Language?

Low-resource languages are languages that have limited digital resources, such as data, tools, and technologies available for natural language processing and computational linguistics. This application aims to support several low-resource languages, providing translation and image generation capabilities.

## Features

- Translate text from any language to English.
- Generate responses in the selected low-resource language based on the translated English text.
- Generate images based on descriptions in any language.
- Detect the input language and provide translated responses.
- Support for multiple low-resource languages through a dropdown selection.

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/langflow-hackathon.git
cd langflow-hackathon
```

### Create a Virtual Environment and Activate It

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install the Required Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Run the Streamlit Application

```bash
streamlit run app.py
```

### Open the Application in Your Browser

Typically available at [http://localhost:8501](http://localhost:8501).

1. Select the mode (Text Mode or Image Mode) and the low-resource language from the dropdown menu.
2. Enter the text you want to translate or describe for image generation.
3. Click the "Submit" button to get the response or generated image.

## Project Structure

- `app.py`: The main Streamlit application file.
- `requirements.txt`: The list of dependencies required for the project.

## API Keys

This application uses several APIs that require authentication. Ensure you have the appropriate API keys and add them to your environment variables or directly in the code:

- OpenAI API key for translations and language detection.
- Replicate API key for image generation.
- Perplexity API key for generating text responses.

## Note

Due to challenges with custom components for Langflow, this project uses Streamlit and OpenAI to achieve the desired functionality.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- Streamlit for the easy-to-use framework for creating web applications.
- OpenAI for the powerful language models.
- Replicate for the image generation API.
- Perplexity for the text generation API.

## Additional Information

This application is an implementation of the prompt engineering technique "Translation Augmented Generation" presented at the LF AI Summit.
