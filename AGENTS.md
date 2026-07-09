## Tech Stack
- Python
- Streamlit (UI)
- LangGraph (orchestration)
- Google Gemini via langchain-google-genai (LLM)
- ElevenLabs speech_to_text (transcription)
- moviepy, mutagen, ffmpeg (media processing)
- python-dotenv (env config)

## Project Structure
- app.py — Streamlit entry point.
- src/audiosummarizer/graph/audio_graph.py — builds LangGraph pipeline.
- src/audiosummarizer/nodes/ — transcribe/summarize node implementations.
- src/audiosummarizer/state/audio_state.py — AudioAnalysisState schema.
- src/audiosummarizer/LLMS/ — Gemini LLM wrapper.
- src/audiosummarizer/ui/ — Streamlit UI modules + config.
- src/audiosummarizer/utils/token_tracker.py — ElevenLabs usage tracking.

## How to Run Tests
n/a

## Conventions
- Keep UI logic in `src/audiosummarizer/ui/`; graph logic in `graph/` and `nodes/`.
- Use `st.error`/`st.warning` for UI-facing errors in try/except blocks.
- Require `GEMINI_API_KEY` before Gemini calls and `ELEVENLABS_API_KEY` before transcription.
- Respect `AudioAnalysisState` fields when reading/writing state.
- Persist ElevenLabs usage via `TokenTracker` JSON in user home.

## What NOT to Do
- Do not add persistent storage for transcripts/summaries (session_state only).
- Do not commit API keys or `.env` files.
- Do not bypass `TokenTracker` when recording ElevenLabs usage.
- Do not mix UI concerns into graph/node modules (or vice versa).