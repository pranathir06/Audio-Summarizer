## Vision
Purpose: Transcribe customer call audio/video, summarize key points, enable Q&A
Users: Customer support analysts handling recorded calls

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| Support Analyst | Manual note-taking from calls | Get structured summaries fast |
| QA Reviewer | Hard to find issues in long calls | Ask targeted questions on transcript |
| Team Lead | Inconsistent call documentation | Standardized call summaries |

## MVP Scope
In Scope:
- Audio/video upload in Streamlit UI
- ElevenLabs transcription with diarization
- Gemini-based structured summary
- Chat Q&A on transcript/summary
- Token usage display for ElevenLabs credits

Out of Scope:
- Authentication or user management
- Persistent storage of transcripts/summaries
- Batch processing or job queues
- Non-Gemini LLM providers

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Requires GEMINI_API_KEY and ELEVENLABS_API_KEY | External LLM and transcription APIs |
| ffmpeg required for video processing | moviepy dependency for video |