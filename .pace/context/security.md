## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| GEMINI_API_KEY | Environment variable | Not committed; required at runtime |
| ELEVENLABS_API_KEY | Environment variable | Not committed; required at runtime |
| Transcripts/summaries | Streamlit session_state | In-memory session only |
| Token usage | ~/.elevenlabs_token_usage.json | Local file in user home |
| Uploaded audio | Temp file on disk | Temporary file path in /tmp or NamedTemporaryFile |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| App | Google Gemini API | API key (GEMINI_API_KEY) |
| App | ElevenLabs API | API key (ELEVENLABS_API_KEY) |

## Security Requirements
- Do not commit .env files or API keys
- Require GEMINI_API_KEY and ELEVENLABS_API_KEY before external API calls
- Avoid persistent storage for transcripts/summaries (session_state only)
- Keep token usage file in user home only

## Security Checklist
API keys sourced from env vars only: pass
No auth/user accounts implemented: pass
Transcript/summary persistence avoided: pass
Temp files used for uploads: pass
