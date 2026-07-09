## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| Audio/video uploads | Temp files on disk | OS temp files; no persistence beyond session |
| Transcripts/summaries | Streamlit session_state | In-memory session; no DB |
| ElevenLabs token usage | ~/.elevenlabs_token_usage.json | Local user file |
| API keys | Environment variables | Not stored in repo |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| Streamlit app | ElevenLabs API | ELEVENLABS_API_KEY env var |
| Streamlit app | Google Gemini API | GEMINI_API_KEY env var |

## Security Requirements
- Do not commit .env files or API keys
- Require GEMINI_API_KEY and ELEVENLABS_API_KEY before external calls
- Keep transcripts/summaries in session_state only (no persistence)
- ffmpeg must be installed for video processing (external dependency)

## Security Checklist
API keys sourced from env: pass
No auth system present: fail
Persistent transcript storage: pass
Temp audio cleanup after video extraction: pass
Token usage file stored in user home: pass