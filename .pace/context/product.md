## Vision
Purpose: Transcribe customer audio calls, summarize key points, enable Q&A.
Users: Customer support analysts, QA reviewers, call center managers.

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| Support Analyst | Long call transcripts to review | Quick structured summaries |
| QA Reviewer | Manual call scoring is slow | Fast access to issues/sentiment |
| Manager | Hard to extract insights from calls | Ask questions about calls |

## MVP Scope
In Scope:
- Upload audio/video files
- ElevenLabs transcription with diarization
- Gemini-based structured summary
- Streamlit chat Q&A over transcript/summary
- Token usage tracking for transcription
Out of Scope:
- User authentication
- Persistent storage of transcripts/summaries
- Batch processing/queues
- Multi-tenant admin dashboards

## Strategic Constraints
| Constraint | Reason |
|---|---|
| API keys required (GEMINI_API_KEY, ELEVENLABS_API_KEY) | External services used |
| No persistent transcript storage | AGENTS.md constraint |
| ffmpeg required for video files | moviepy depends on ffmpeg |