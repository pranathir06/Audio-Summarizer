## Tech Stack
- Python
- Streamlit (UI)
- LangGraph, LangChain (orchestration)
- Google Gemini via langchain-google-genai (LLM)
- ElevenLabs speech_to_text (transcription)
- moviepy, mutagen, ffmpeg (media)
- python-dotenv (env config)

## Project Structure
- app.py: Streamlit entrypoint, calls load_langgraph_agenticai_app()
- src/audiosummarizer/LLMS/: Gemini client wrappers
- src/audiosummarizer/graph/: LangGraph builder (AudioGraphBuilder)
- src/audiosummarizer/nodes/: graph nodes (transcribe/summarize)
- src/audiosummarizer/state/: AudioAnalysisState schema
- src/audiosummarizer/ui/: Streamlit UI + config (uiconfigfile.ini)
- src/audiosummarizer/ui/streamlitui/: pages/widgets
- src/audiosummarizer/utils/: token usage tracking

## How to Run Tests
n/a

## Conventions
- Keep UI logic in src/audiosummarizer/ui/; graph logic in graph/ and nodes/.
- Use AudioAnalysisState fields consistently (audio_path, transcript, summary, audio_duration_seconds).
- Handle UI errors with try/except and st.error/st.warning.
- Require GEMINI_API_KEY and ELEVENLABS_API_KEY before external calls.
- Store transcripts/summaries only in Streamlit session_state.

## What NOT to Do
- Do not add persistent storage for transcripts or summaries.
- Do not add new LLM providers beyond Gemini.
- Do not commit .env files or API keys.
- Do not bypass API-key checks for Gemini/ElevenLabs.
- Do not mix UI concerns into graph/node code.