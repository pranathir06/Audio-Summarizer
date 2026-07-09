## Vision
Purpose: Transcribe customer audio calls, summarize them, and enable Q&A on the content
Users: Customer support analysts or teams reviewing customer calls
## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| Support Analyst | Long calls to review manually | Get structured summaries and key points fast |
| Support Manager | Need insights from call content | Ask questions about transcript/summary |
| QA/Compliance Reviewer | Hard to scan full audio | Access transcript with speaker labels |
## MVP Scope
In Scope:
- Audio/video upload via Streamlit
- ElevenLabs transcription with diarization
- Gemini-generated structured summaries
- Interactive chat Q&A over transcript/summary
Out of Scope:
- Persistent storage of transcripts/summaries
- Multi-user auth or accounts
- Non-Streamlit UI
## Strategic Constraints
| Constraint | Reason |
|---|---|
| Require GEMINI_API_KEY and ELEVENLABS_API_KEY env vars | External API usage in Gemini/ElevenLabs clients |
| ffmpeg required for video processing | moviepy depends on ffmpeg for video/audio extraction |
| No persistent storage for transcripts/summaries | AGENTS.md constraint |
