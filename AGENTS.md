## Tech Stack
- Python (pip)
- Streamlit (UI)
- LangGraph (orchestration)
- Google Gemini via langchain-google-genai (LLM)
- ElevenLabs speech_to_text (transcription)
- moviepy, mutagen, ffmpeg (media processing)
- python-dotenv (env config)

## Project Structure
- app.py: Streamlit entry point.
- src/audiosummarizer/graph/audio_graph.py: builds LangGraph pipeline.
- src/audiosummarizer/nodes/: transcribe_node & summarize_node logic.
- src/audiosummarizer/state/audio_state.py: AudioAnalysisState schema.
- src/audiosummarizer/ui/: UI config and Streamlit screens.
- src/audiosummarizer/ui/streamlitui/chat_interface.py: Q&A over transcript/summary.
- src/audiosummarizer/LLMS/: Gemini wrapper.
- src/audiosummarizer/utils/token_tracker.py: ElevenLabs usage tracking.

## How to Run Tests
n/a

## Conventions
- Keep UI logic in `ui/` and graph/node logic in `graph/`/`nodes/`.
- Require `GEMINI_API_KEY` and `ELEVENLABS_API_KEY` before API calls.
- Use `st.error`/`st.warning` for UI error handling in try/except.
- Respect `AudioAnalysisState` fields when passing state.
- Persist ElevenLabs usage via `TokenTracker` JSON in user home.

## What NOT to Do
- Do not store transcripts/summaries outside Streamlit `session_state`.
- Do not commit `.env` files or API keys.
- Do not add auth/login or persistent storage features (out of scope).
- Do not bypass ffmpeg-based media handling for video inputs.
- Do not scatter UI logic into graph/nodes modules.