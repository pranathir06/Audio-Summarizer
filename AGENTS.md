## Tech Stack
- Python (pip)
- Streamlit (UI)
- LangGraph (workflow orchestration)
- Google Gemini via langchain-google-genai (LLM)
- ElevenLabs speech_to_text (transcription)
- moviepy, mutagen, ffmpeg (media handling)
- python-dotenv (env loading)
- pytest (test runner, not configured)

## Project Structure
- app.py: Streamlit entry point (only supported entry).
- src/audiosummarizer/LLMS/geminillm.py: Gemini client/config.
- src/audiosummarizer/graph/audio_graph.py: LangGraph StateGraph builder.
- src/audiosummarizer/nodes/: graph nodes (file, transcribe, summarize).
- src/audiosummarizer/state/audio_state.py: AudioAnalysisState schema.
- src/audiosummarizer/ui/: Streamlit UI config and views.
- src/audiosummarizer/utils/: token usage tracking.

## How to Run Tests
n/a

## Conventions
- Keep UI logic in `src/audiosummarizer/ui/`; graph logic in `graph/` and `nodes/`.
- Use `AudioAnalysisState` fields exactly as defined.
- Require `GEMINI_API_KEY` and `ELEVENLABS_API_KEY` before any external calls.
- Store transcripts/summaries only in `st.session_state` (no persistence).
- Add try/except error handling in Streamlit flows.

## What NOT to Do
- Do not add non-Streamlit entry points or bypass `app.py`.
- Do not commit API keys or `.env` files.
- Do not persist transcripts/summaries to disk or external storage.
- Do not remove/ignore `ffmpeg` dependency for video processing.
- Do not change API key requirements for Gemini/ElevenLabs.