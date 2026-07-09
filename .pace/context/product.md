## Vision
Purpose: Transcribe customer audio calls, summarize them, and enable Q&A
Users: Customer support teams analyzing call recordings

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| Support Analyst | Long calls are time-consuming to review | Get structured summaries quickly |
| QA Reviewer | Needs evidence for coaching | Ask questions about call details |
| Support Manager | Wants sentiment and action tracking | See concise issue/context/actions/sentiment |

## MVP Scope
In Scope:
- Audio/video upload in Streamlit UI
- ElevenLabs transcription with diarization
- Gemini summary with structured sections
- Chat Q&A over transcript and summary
- Token usage tracking for transcription

Out of Scope:
- User authentication
- Persistent storage for transcripts/summaries
- Batch processing or job queues
- Multi-usecase workflows beyond audio summarizer

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Requires GEMINI_API_KEY and ELEVENLABS_API_KEY | External API dependencies |
| ffmpeg needed for video files | moviepy relies on ffmpeg |
| Session-only storage | Design note in AGENTS.md |
