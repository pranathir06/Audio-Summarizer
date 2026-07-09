## Tech Stack
- Python
- Streamlit (UI)
- LangGraph (langgraph) for orchestration
- Google Gemini via langchain-google-genai
- ElevenLabs speech_to_text
- moviepy, mutagen, ffmpeg (external)
- python-dotenv
- pytest (test runner; no tests configured)

## Project Structure
- app.py: Streamlit entry point
- src/audiosummarizer/: core package
- src/audiosummarizer/LLMS/geminillm.py: Gemini client config
- src/audiosummarizer/graph/audio_graph.py: LangGraph workflow (START→END)
- src/audiosummarizer/nodes/: transcription/summarization nodes
- src/audiosummarizer/state/audio_state.py: AudioAnalysisState schema
- src/audiosummarizer/ui/: Streamlit UI config/components
- src/audiosummarizer/utils/: token usage tracking

## How to Run Tests
n/a

## Conventions
- Keep UI logic in `ui/`; graph orchestration in `graph/` and `nodes/`.
- Use `AudioAnalysisState` fields exactly as defined.
- Require `GEMINI_API_KEY` and `ELEVENLABS_API_KEY` before API calls.
- Store transcripts/summaries only in `st.session_state` (no persistence).
- Add try/except error handling in Streamlit flows.

## What NOT to Do
- Do not commit API keys or `.env` files.
- Do not write transcripts/summaries to disk or databases.
- Do not bypass required env var checks for Gemini/ElevenLabs.
- Do not move UI logic into graph/node modules or vice versa.