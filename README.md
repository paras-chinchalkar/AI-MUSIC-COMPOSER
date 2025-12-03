# AI Music Composer

An AI-powered music composition app using Streamlit, LangChain, and the Groq API.

## Setup Instructions

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/paras-chinchalkar/AI-MUSIC-COMPOSER.git
   cd AI-MUSIC-COMPOSER
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your Groq API key:**
   - Create `.streamlit/secrets.toml` in the project root
   - Add your Groq API key:
     ```toml
     GROQ_API_KEY = "your-groq-api-key-here"
     ```
   - Get your API key from [Groq Console](https://console.groq.com)

5. **Run the app:**
   ```bash
   streamlit run app.py
   ```

### Streamlit Cloud Deployment

1. **Go to [Streamlit Cloud](https://streamlit.io/cloud)**

2. **Connect your GitHub repository**

3. **In the app settings, add the secret:**
   - Click "Advanced settings" → "Secrets"
   - Add:
     ```
     GROQ_API_KEY = "your-groq-api-key-here"
     ```

4. **The app will deploy and use the secret automatically**

## Features

- **Melody Generation**: AI-powered melody creation based on text descriptions
- **Harmony Generation**: Automatic harmony chord generation
- **Rhythm Generation**: Dynamic rhythm pattern creation
- **Style Adaptation**: Adapt compositions to different musical styles (Sad, Happy, Jazz, Romantic, Extreme)
- **Audio Synthesis**: Generate WAV audio from musical notes

## Technologies

- **Streamlit**: Web app framework
- **LangChain**: AI orchestration
- **Groq API**: Fast LLM inference
- **Music21**: Music theory and note handling
- **Synthesizer**: Audio generation
- **SciPy**: Audio processing

## License

MIT
