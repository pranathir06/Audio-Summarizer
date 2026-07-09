## Vision
Purpose: Summarize customer call audio into transcript, summary, and Q&A responses
Users: Customer support analysts handling recorded calls

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| Support Analyst | Long calls to review manually | Fast, structured call summaries |
| Team Lead | Needs consistent call insights | Standardized summaries and sentiment |
| QA Reviewer | Hard to find specific details | Searchable transcript + Q&A |

## MVP Scope
In Scope:
- Upload audio/video file
- Transcribe with diarization
- Summarize into structured sections
- Chat Q&A over transcript+summary
- Token usage display for ElevenLabs

Out of Scope:
- User authentication
- Persistent storage of transcripts/summaries
- Batch processing or queues
- Removing ffmpeg dependency for video handling

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Requires GEMINI_API_KEY | Gemini LLM access required (GeminiLLM) |
| Requires ELEVENLABS_API_KEY | ElevenLabs transcription required (transcribe_node) |
| ffmpeg for video | MoviePy uses ffmpeg for video audio extraction |
| Session-only data | Results stored in Streamlit session_state only |
