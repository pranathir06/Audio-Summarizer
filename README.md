### Customer Audio Summarizer - Agentic AI Application

An intelligent audio processing application that transcribes customer audio calls, generates AI-powered summaries, and allows interactive Q&A about the audio content.

#### Features
- 🎤 **Audio Transcription**: Automatically transcribes audio files using ElevenLabs
- 📋 **AI Summarization**: Generates structured summaries of customer calls
- 💬 **Interactive Chat**: Ask questions about the uploaded audio content
- 🎨 **Modern UI**: Beautiful Streamlit interface with real-time processing

#### Requirements
- Python 3.8+
- GEMINI_API_KEY environment variable
- ELEVENLABS_API_KEY environment variable
- **ffmpeg** (for video file processing - optional but recommended)
  - **macOS**: `brew install ffmpeg`
  - **Linux**: `sudo apt-get install ffmpeg`
  - **Windows**: Download from https://ffmpeg.org/download.html

#### How to Use
1. Install requirements: `pip install -r requirements.txt`
2. Set up environment variables (GEMINI_API_KEY and ELEVENLABS_API_KEY)
3. Run the application: `streamlit run app.py`
4. Upload an audio file
5. Wait for transcription and summary
6. Ask questions about the audio content in the chat interface

#### Chat Features
After uploading and processing an audio file, you can ask questions like:
- "What was the customer's main concern?"
- "How did the customer feel about the service?"
- "What actions were taken during the call?"
- "Summarize the key points discussed"
- Any other questions about the audio content

### End to End Project Agentic AI Chatbots