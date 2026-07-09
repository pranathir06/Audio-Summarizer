## Tech Stack
- Python (pip)
- Streamlit (UI)
- LangGraph (langgraph orchestration)
- Google Gemini via langchain-google-genai
- ElevenLabs speech_to_text
- moviepy, mutagen, ffmpeg (external)
- python-dotenv

## Project Structure
- app.py: Streamlit entry point; calls load_langgraph_agenticai_app()
- src/audiosummarizer/state/audio_state.py: AudioAnalysisState schema
- src/audiosummarizer/graph/audio_graph.py: AudioGraphBuilder.setup_graph()
- src/audiosummarizer/nodes/: LangGraph node implementations (transcribe/summarize)
- src/audiosummarizer/LLMS/geminillm.py: Gemini client/config (GEMINI_API_KEY/MODEL)
- src/audiosummarizer/ui/: Streamlit UI flow and config
- src/audiosummarizer/utils/token_tracker.py: ElevenLabs token usage file

## How to Run Tests
n/a

## Conventions
- Keep Streamlit UI logic in ui/ modules; graph logic in graph/ and nodes/.
- Use try/except with Streamlit error handling in UI flows.
- Respect AudioAnalysisState field names and types.
- Require GEMINI_API_KEY and ELEVENLABS_API_KEY before external API calls.
- Use session_state for transcript/summary (no persistence).

## What NOT to Do
- Do not add persistent storage for transcripts/summaries.
- Do not commit .env files or API keys.
- Do not bypass ffmpeg requirement for video handling.
- Do not move UI logic into graph/nodes or vice versa.
- Do not change AudioAnalysisState fields without updating all consumers.