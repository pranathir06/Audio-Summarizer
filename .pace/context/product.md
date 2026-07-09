## Vision
Purpose: Summarize customer audio calls with transcription, structured summary, and Q&A
Users: Customer support teams analyzing call recordings

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| Support Analyst | Time-consuming manual call review | Get quick, structured summaries |
| QA Manager | Hard to audit call quality at scale | Ask targeted questions about calls |
| Team Lead | Limited visibility into customer issues | Surface key issues and sentiment fast |

## MVP Scope
In Scope:
- Audio/video upload in Streamlit UI
- ElevenLabs transcription with diarization
- Gemini LLM structured summary
- Chat Q&A over transcript/summary
- Token usage display for transcription credits
Out of Scope:
- Multi-user auth and accounts
- Persistent storage of transcripts/summaries
- Batch processing or job queues
- Non-English transcription support

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Requires GEMINI_API_KEY | Gemini LLM initialization enforces env var |
| Requires ELEVENLABS_API_KEY | ElevenLabs transcription client uses API key |
| ffmpeg needed for video files | moviepy requires ffmpeg for extraction |
