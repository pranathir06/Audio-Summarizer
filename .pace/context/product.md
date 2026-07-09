## Vision
Purpose: Transcribe customer audio calls, generate summaries, enable Q&A on audio content
Users: Streamlit users uploading customer audio/video files for summarization

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| Customer support analyst | Manual review of call recordings | Get transcript and structured summary quickly |
| QA/review user | Hard to search call content | Ask questions about the call via chat |

## MVP Scope
In Scope:
- Audio/video file upload in Streamlit UI
- ElevenLabs transcription with diarization
- Gemini-based structured summary
- Interactive chat over transcript/summary
Out of Scope:
- Persistent storage of transcripts/summaries
- Non-Streamlit entry points

## Strategic Constraints
| Constraint | Reason |
|---|---|
| GEMINI_API_KEY required | Gemini LLM calls in GeminiLLM |
| ELEVENLABS_API_KEY required | ElevenLabs transcription in transcribe_node |
| ffmpeg required for video | moviepy uses ffmpeg for video/audio extraction |
| Streamlit app entry only (app.py) | AGENTS.md guidance |