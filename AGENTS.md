## Tech Stack
- Python
- Streamlit (UI)
- LangGraph (langgraph) for orchestration
- Google Gemini via langchain-google-genai
- ElevenLabs speech_to_text
- moviepy, mutagen; ffmpeg (external)
- python-dotenv
- pytest (runner listed, but tests n/a)

## Project Structure
- app.py — Streamlit entry; calls load_langgraph_agenticai_app()
- src/audiosummarizer/state/audio_state.py — AudioAnalysisState schema
- src/audiosummarizer/graph/audio_graph.py — AudioGraphBuilder.setup_graph()
- src/audiosummarizer/nodes/ — LangGraph node implementations (transcribe/summarize)
- src/audiosummarizer/LLMS/geminillm.py — Gemini client/config
- src/audiosummarizer/ui/ — Streamlit UI logic and components
- src/audiosummarizer/utils/token_tracker.py — ElevenLabs token usage tracking
- src/audiosummarizer/ui/uiconfigfile.ini — UI options/config

## How to Run Tests
n/a

## Conventions
- Keep Streamlit UI logic inside src/audiosummarizer/ui; graph logic in graph/ and nodes/
- Respect AudioAnalysisState field names/types when passing state
- Require GEMINI_API_KEY and ELEVENLABS_API_KEY before external API calls
- Use Streamlit try/except error handling in UI flows
- Store transcripts/summaries only in Streamlit session_state

## What NOT to Do
- Do not commit .env files or API keys
- Do not add persistent storage for transcripts/summaries
- Do not bypass API key checks for Gemini/ElevenLabs
- Do not move UI logic into graph/nodes or vice versa
- Do not remove ffmpeg-based video handling requirements