## Vision
Purpose: Transcribe customer audio calls, summarize key points, and answer questions about the call
Users: Customer support analysts, QA reviewers, and ops teams working with call recordings

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| Support Analyst | Manual note-taking from long calls | Get structured summaries quickly |
| QA Reviewer | Hard to audit large volumes of calls | Extract key issues and actions fast |
| Ops Manager | Need searchable insights from calls | Ask follow-up questions on call content |

## MVP Scope
In Scope:
- Upload audio/video files in Streamlit UI
- Transcribe via ElevenLabs with speaker labels
- Summarize via Gemini into structured sections
- Chat Q&A based on transcript + summary
- Token usage tracking for ElevenLabs seconds

Out of Scope:
- Authentication or user accounts
- Persistent storage of transcripts/summaries beyond session_state
- Batch processing or job queues
- Additional LLM providers beyond Gemini

## Strategic Constraints
| Constraint | Reason |
|---|---|
| GEMINI_API_KEY required | GeminiLLM enforces API key check |
| ELEVENLABS_API_KEY required | Transcription uses ElevenLabs API |
| ffmpeg required for video | moviepy relies on ffmpeg for video handling |
| No long-term storage | AGENTS.md prohibits persistent storage for transcripts/summaries |
