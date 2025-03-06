"""
### Code Summary:
This script sets up a summarization application using the Hugging Face Transformers library and the Gradio interface.
The app will take input text from the user, summarize it using a pre-trained BART model, and display the result after the user clicks the "Summarize" button.
"""

# Step 1: Code to ignore warnings
from transformers.utils import logging
logging.set_verbosity_error()

# Step 2: Import necessary libraries
from transformers import pipeline
import gradio as gr

"""
## Step 3: Initialize the Summarization Pipeline

We use the BART model fine-tuned for summarization. The model is automatically downloaded when the pipeline is created. 
"""

# Initialize the summarizer object with a pre-trained BART model
summarizer = pipeline(task="summarization", model="facebook/bart-large-cnn")

# Example text for summarization
example_text = """BART is a transformer encoder-encoder (seq2seq) model with a bidirectional (BERT-like) encoder and an autoregressive (GPT-like) decoder.
BART is pre-trained by (1) corrupting text with an arbitrary noising function, and (2) learning a model to reconstruct the original text.
BART is particularly effective when fine-tuned for text generation (e.g. summarization, translation) but also works well for comprehension tasks (e.g. text classification, question answering).
This particular checkpoint has been fine-tuned on CNN Daily Mail, a large collection of text-summary pairs."""

# Step 4: Define the summarization function
def summarize_text(input_text):
    """
    Summarizes the input text using the pre-trained BART model.
    
    Args:
        input_text (str): The text to be summarized.
        
    Returns:
        str: The summarized text.
    """
    summary = summarizer(
        input_text,
        repetition_penalty=5.0,  # Discourages repetition in the summary
        length_penalty=0.3,      # Adjusts summary length
        min_length=20, max_length=100  # Defines the length range for the summary
    )
    return summary[0]["summary_text"]

# Step 5: Define Gradio interface

# Create the Gradio interface with a button to trigger summarization
interface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(label="Input Text", placeholder="Enter your text here..."),
    outputs=gr.Textbox(label="Summary"),
    title="Text Summarizer with BART",
    description="Enter a piece of text and click the button to get the summary.",
    live=False  # Set live=False so the summary is generated only after button click
)

# Step 6: Launch the Gradio UI
interface.launch(share=True)
