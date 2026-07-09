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
- src/audiosummarizer/graph/audio_graph.py — builds LangGraph via AudioGraphBuilder
- src/audiosummarizer/nodes/ — graph node implementations (transcribe, summarize, etc.)
- src/audiosummarizer/state/audio_state.py — AudioAnalysisState schema
- src/audiosummarizer/LLMS/geminillm.py — Gemini client/config
- src/audiosummarizer/ui/ — Streamlit UI modules and config
- src/audiosummarizer/utils/token_tracker.py — ElevenLabs token tracking

## How to Run Tests
n/a

## Conventions
- Keep Streamlit UI logic in `src/audiosummarizer/ui/`; graph logic in `graph/` and `nodes/`.
- Use try/except error handling for Streamlit UI flows.
- Respect `AudioAnalysisState` field names and types.
- Require `GEMINI_API_KEY` and `ELEVENLABS_API_KEY` before calling external APIs.
- Use Streamlit session_state for transient transcript/summary data.

## What NOT to Do
- Do not add persistent storage for transcripts/summaries or user data.
- Do not commit API keys or `.env` files.
- Do not bypass required API key checks for Gemini/ElevenLabs.
- Do not move UI code into graph/nodes or vice versa.
- Do not remove ffmpeg-based handling for video inputs.