# Text Summarizer App

## Description
The **Text Summarizer App** is a web application that uses artificial intelligence to summarize long pieces of text into concise summaries. The app uses the **BART (Bidirectional and Auto-Regressive Transformers)** model from Hugging Face for high-quality text summarization.

## Features
- Input a block of text to summarize.
- AI-powered text summarization using the BART model.
- Simple, user-friendly interface built with Gradio.
- Option to adjust summary length and repetition penalty.

## Technologies Used
- **Programming Language**: Python 3.7+
- **AI Model**: Facebook BART (BART-Large-CNN)
- **Web Interface**: Gradio
- **Libraries**: Hugging Face Transformers, Gradio

## Libraries and Dependencies
- transformers: Hugging Face library for pre-trained models like BART
- gradio: For building the web interface

To install the necessary packages, run:
```bash
pip install transformers gradio
```

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/text-summarizer-app.git
   cd text-summarizer-app
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install transformers gradio
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. Open a web browser and navigate to `http://127.0.0.1:7860` to access the app.

3. Enter or paste the text you want to summarize in the input box.

4. Click the **Submit** button to generate the summary.

## Configuration

You can modify the following parameters in the `app.py` file:

- **repetition_penalty**: Controls the penalty for repetition (default: 5.0).
- **length_penalty**: Controls the length of the summary (default: 0.3).
- **min_length**: Minimum length of the summary (default: 20).
- **max_length**: Maximum length of the summary (default: 100).

## Contributing

Contributions to improve the Text Summarizer App are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- **Hugging Face** for providing the BART model.
- **Gradio** for building the easy-to-use interface.

## Disclaimer

This tool is designed to assist with summarizing text, but always review the generated summary for accuracy and relevance before using it.
