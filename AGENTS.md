## Tech Stack
- Python
- Streamlit (UI)
- LangGraph (langgraph) for orchestration
- Google Gemini via langchain-google-genai
- ElevenLabs speech_to_text
- moviepy, mutagen, ffmpeg (external)
- python-dotenv

## Project Structure
- app.py — Streamlit entry point; calls load_langgraph_agenticai_app()
- src/audiosummarizer/LLMS/geminillm.py — Gemini client config (GEMINI_API_KEY/GEMINI_MODEL)
- src/audiosummarizer/graph/audio_graph.py — LangGraph builder
- src/audiosummarizer/nodes/ — graph node implementations (transcribe/summarize)
- src/audiosummarizer/state/audio_state.py — AudioAnalysisState schema
- src/audiosummarizer/ui/ — Streamlit UI config & components
- src/audiosummarizer/utils/token_tracker.py — ElevenLabs token usage tracking

## How to Run Tests
n/a

## Conventions
- Keep Streamlit UI logic in `ui/`; graph logic in `graph/` and `nodes/`.
- Use `AudioAnalysisState` fields exactly as defined (audio_path, transcript, summary, audio_duration_seconds).
- Add try/except error handling in UI flows (Streamlit).
- Require `GEMINI_API_KEY` and `ELEVENLABS_API_KEY` before external API calls.
- Store transcripts/summaries only in `st.session_state` (no persistence).

## What NOT to Do
- Do not commit API keys or .env files.
- Do not add persistent storage for transcripts/summaries.
- Do not bypass ffmpeg requirements for video handling.
- Do not introduce new entry points besides Streamlit `app.py`.
- Do not mix UI code into graph/node modules.