## Tech Stack
- Python (pip)
- Streamlit (UI)
- LangGraph (orchestration)
- Google Gemini via langchain-google-genai (LLM)
- ElevenLabs speech_to_text (transcription)
- moviepy, mutagen, ffmpeg (audio/video processing)
- python-dotenv (env config)

## Project Structure
- app.py: Streamlit entry point calling load_langgraph_agenticai_app()
- src/audiosummarizer/graph/audio_graph.py: LangGraph builder (audio_file → transcribe → summarize)
- src/audiosummarizer/nodes/: graph node implementations
- src/audiosummarizer/state/audio_state.py: AudioAnalysisState schema
- src/audiosummarizer/ui/: Streamlit UI components and config
- src/audiosummarizer/LLMS/: LLM client wrappers
- src/audiosummarizer/utils/: token usage tracking

## How to Run Tests
n/a

## Conventions
- Use Streamlit error handling (st.error/st.warning) with try/except in UI flows.
- Respect AudioAnalysisState fields: audio_path, transcript, summary, audio_duration_seconds.
- Require GEMINI_API_KEY and ELEVENLABS_API_KEY before invoking external APIs.
- Persist token usage via TokenTracker (JSON in user home).
- Keep Streamlit UI logic in ui/ modules; graph logic in graph/ and nodes/.

## What NOT to Do
- Do not commit .env files or API keys.
- Do not add persistent storage for transcripts/summaries (session_state only).
- Do not introduce batch processing, job queues, or auth features.
- Do not remove ffmpeg dependency for video handling.