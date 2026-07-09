## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| GEMINI_API_KEY | Environment variable | Not in repo; loaded via dotenv |
| ELEVENLABS_API_KEY | Environment variable | Not in repo; loaded via dotenv |
| Audio/video files | Temporary file in OS temp dir | Deleted after processing; retained for chat session |
| Transcript/summary | Streamlit session_state | In-memory per session |
| Token usage data | ~/.elevenlabs_token_usage.json | Local file in user home |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| Streamlit app | Google Gemini API | API key (GEMINI_API_KEY) |
| Streamlit app | ElevenLabs speech_to_text | API key (ELEVENLABS_API_KEY) |

## Security Requirements
- Do not commit .env files or API keys
- Require GEMINI_API_KEY and ELEVENLABS_API_KEY before API calls
- Do not add persistent storage for transcripts/summaries

## Security Checklist
No API keys in repo: pass
External APIs require keys: pass
Local token file stored in home dir: pass
Session-only transcript storage: pass