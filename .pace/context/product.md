## Vision
Purpose: Transcribe customer audio calls, summarize them, and enable Q&A on content
Users: Customer support analysts or teams reviewing call recordings

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| Support Analyst | Long call recordings are time-consuming to review | Get structured summaries and key issues fast |
| Team Lead | Needs quick insights from customer calls | Review summaries and sentiment for coaching |
| QA Reviewer | Must audit call quality | Search transcript via Q&A for specific details |

## MVP Scope
In Scope:
- Upload audio/video file in Streamlit UI
- Transcribe using ElevenLabs (with diarization)
- Summarize transcript via Gemini with structured sections
- Chat Q&A using transcript and summary
- Token usage tracking for transcription time

Out of Scope:
- User authentication or roles
- Persistent storage for transcripts/summaries
- Batch processing or job queues
- Removing ffmpeg dependency for video

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Requires GEMINI_API_KEY and ELEVENLABS_API_KEY | External LLM and transcription services |
| ffmpeg required for video processing | moviepy depends on ffmpeg |
| No persistent data storage | AGENTS.md: session_state only; no DB |
| Streamlit UI only | app.py entry point is Streamlit |
