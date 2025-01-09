# Gemini AI

Gemini AI is an advanced AI-powered web application that provides a suite of services, including a chatbot, image captioning, text embedding, and a Q&A feature. The application is built using **[Streamlit](https://docs.streamlit.io/)**, leveraging the **Gemini Pro** model from Google’s generative AI capabilities.

## Features

### 1. ChatBot

- Engage with the Gemini Pro chatbot, capable of understanding and generating human-like text responses.
- The chat history is displayed to maintain the conversation context.

### 2. Image Captioning:

- Upload an image and receive a descriptive caption generated by the Gemini AI model.
- Supports `.jpg`, `.jpeg`, and `.png` file formats.

### 3. Text Embedding:

- Input text to generate embeddings useful for document retrieval and other NLP tasks.
- Embeddings are displayed as a list of floating-point numbers.

### 4. Ask Me Anything:

- Pose any question, and the Gemini AI model will generate an informative answer.

## Project Structure

- `main.py`: The main file that sets up the Streamlit app and handles navigation between the different services offered.
- `streamlit_util.py`: Contains utility functions used across the Streamlit app for layout and styling.
- `gemini_util.py`: Contains utility functions for interacting with the Gemini AI models, including loading models, generating captions, embedding text, and handling user prompts.

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/username/gemini-ai.git
cd gemini-ai
```

### 2. Install the required dependencies:

- Ensure you have Python 3.8 or above. Install dependencies using `pip`.

  ```bash
  pip install -r requirements.txt
  ```

### 3. Set up your environment:

- You'll need an API key from Google’s generative AI services. Set it up in your environment.

  ```bash
  export API_KEY='your_api_key_here'
  ```

### 4. Run the application:

- Start the Streamlit app.

  ```bash
  streamlit run main.py
  ```

## Usage

- ChatBot: Select the "ChatBot" option from the sidebar to interact with the AI chatbot.
- Image Captioning: Upload an image in the "Image Captioning" section to receive a descriptive caption.
- Text Embedding: Enter a piece of text in the "Embed text" section to get embeddings.
- Ask Me Anything: Pose a question in the "Ask Me Anything" section to get an answer.

## Requirements

- Python 3.8+
- Streamlit
- Pillow
- Google Generative AI SDK
- streamlit-option-menu

Check out [requirements.txt](requirements.txt) for more details.

## Deployment link

#### [Check it out!](https://gemini-ai-6pieo6evhzghyj5rgazsje.streamlit.app/)


## License

This project is licensed under the [MIT](https://opensource.org/license/mit/) License. Check the [LICENSE](LICENSE) file for more details.

