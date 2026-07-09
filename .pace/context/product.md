## Vision
Purpose: Transcribe customer audio calls, generate AI summaries, and enable Q&A about call content
Users: Customer support analysts / teams handling call recordings

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| Support Analyst | Long call recordings take time to review | Get structured summaries fast |
| Support Manager | Needs insights from calls for QA | Review key issues, actions, sentiment |
| Agent | Needs details from a call | Ask questions about transcript content |

## MVP Scope
In Scope:
- Upload audio/video files via Streamlit
- Transcribe using ElevenLabs (diarized speaker labels)
- Summarize transcript with structured bullets
- Chat Q&A using transcript + summary
- Token usage tracking for ElevenLabs
Out of Scope:
- Persistent storage of transcripts/summaries
- User authentication/authorization
- Batch processing or job queues
- Replacing ffmpeg for video handling

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Require GEMINI_API_KEY and ELEVENLABS_API_KEY | External API access in geminillm.py/transcribe_node.py |
| Use Streamlit UI | app.py entry point + UI modules |
| No persistent storage | AGENTS.md: session_state only |
| ffmpeg required for video | README.md + transcribe_node.py error handling |
