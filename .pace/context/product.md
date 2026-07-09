## Vision
Purpose: Summarize customer audio calls with transcripts, structured summaries, and Q&A
Users: Customer support analysts and teams reviewing call recordings

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| Support Analyst | Long call recordings are time-consuming to review | Get concise summaries and key points fast |
| QA/Training Lead | Needs evidence of agent performance and customer sentiment | Extract actions taken and sentiment cues |
| Manager | Limited time to scan call details | High-level understanding of issues and outcomes |

## MVP Scope
In Scope:
- Upload audio/video files in Streamlit
- Transcription via ElevenLabs with diarization
- Structured summary via Gemini LLM
- Q&A chat over transcript/summary
- Token usage tracking for ElevenLabs

Out of Scope:
- Auth/login or user management
- Persistent storage of transcripts/summaries
- Batch processing or job queues
- Multi-usecase workflows beyond audio summarizer

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Requires GEMINI_API_KEY and ELEVENLABS_API_KEY | External API dependencies |
| ffmpeg needed for video processing | moviepy relies on ffmpeg |
| Session-state only storage | AGENTS.md restriction |
| Streamlit UI only | App entrypoint is app.py running Streamlit |