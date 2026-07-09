## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| Audio files | Temp files on local disk | Temp file lifecycle; not deleted until chat complete |
| Transcripts | Streamlit session_state | In-memory session state |
| Summaries | Streamlit session_state | In-memory session state |
| ElevenLabs usage data | ~/.elevenlabs_token_usage.json | Local JSON file |
| API keys | Environment variables | .env supported via python-dotenv; .gitignore excludes .env |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| Streamlit app | ElevenLabs API | ELEVENLABS_API_KEY |
| Streamlit app | Gemini API (Google) | GEMINI_API_KEY |

## Security Requirements
- Do not commit .env or API keys (.gitignore includes .env)
- Ensure GEMINI_API_KEY and ELEVENLABS_API_KEY are set before runtime
- Install ffmpeg securely when enabling video processing

## Security Checklist
Secrets in repo: Fail
Env vars required: Pass
External API calls authenticated: Pass
Local token file persisted: Pass
