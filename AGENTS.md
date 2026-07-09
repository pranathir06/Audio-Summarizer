## Tech Stack
- Python
- Streamlit (UI)
- LangGraph (orchestration)
- Google Gemini via langchain-google-genai (LLM)
- ElevenLabs speech_to_text (transcription)
- moviepy, mutagen, ffmpeg (media processing)
- python-dotenv (env config)

## Project Structure
- app.py: Streamlit entry point.
- src/audiosummarizer/graph/audio_graph.py: builds LangGraph pipeline.
- src/audiosummarizer/nodes/: transcribe_node and summarize_node logic.
- src/audiosummarizer/state/audio_state.py: AudioAnalysisState schema.
- src/audiosummarizer/LLMS/geminillm.py: Gemini wrapper.
- src/audiosummarizer/ui/streamlitui/: UI screens + chat interface.
- src/audiosummarizer/ui/uiconfigfile.ini: UI config.
- src/audiosummarizer/utils/token_tracker.py: ElevenLabs usage tracking.

## How to Run Tests
n/a

## Conventions
- Keep UI logic in src/audiosummarizer/ui and graph logic in graph/ and nodes/.
- Require GEMINI_API_KEY and ELEVENLABS_API_KEY before API calls.
- Use AudioAnalysisState fields consistently (audio_path, transcript, summary, audio_duration_seconds).
- In Streamlit UI, handle failures with st.error/st.warning.

## What NOT to Do
- Do not commit API keys or .env files.
- Do not persist transcripts/summaries outside Streamlit session_state.
- Do not move chat/summary logic into UI modules or vice versa.
- Do not bypass TokenTracker when recording ElevenLabs usage.