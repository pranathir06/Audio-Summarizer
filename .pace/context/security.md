## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| GEMINI_API_KEY | Environment variable | Required at runtime (geminillm.py) |
| ELEVENLABS_API_KEY | Environment variable | Required at runtime (transcribe_node.py) |
| Audio files | Temp files on disk | Temporary file paths via tempfile; not persisted in app storage |
| Transcripts/Summaries | Streamlit session_state | In-memory session state only |
| ElevenLabs token usage | ~/.elevenlabs_token_usage.json | Local file in user home (token_tracker.py) |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| Streamlit app | Google Gemini API | API key via GEMINI_API_KEY |
| Streamlit app | ElevenLabs API | API key via ELEVENLABS_API_KEY |

## Security Requirements
- Do not commit .env files or API keys (AGENTS.md)
- Require GEMINI_API_KEY and ELEVENLABS_API_KEY before external calls
- Keep transcripts/summaries in session_state only (no persistent storage)

## Security Checklist
Env keys present: fail
API keys committed: fail
Persistent transcript storage: fail
ffmpeg installed for video: fail
