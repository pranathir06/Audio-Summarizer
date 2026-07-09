## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| GEMINI_API_KEY | Environment variable | Not stored in repo; required at runtime |
| ELEVENLABS_API_KEY | Environment variable | Not stored in repo; required at runtime |
| Audio files | Temp files on disk | Stored in system temp; cleanup for video extraction; audio temp kept for chat |
| Token usage data | ~/.elevenlabs_token_usage.json | Local file with usage totals |
| Transcripts/Summaries | Streamlit session_state | In-memory for current session only |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| App (transcribe_node) | ElevenLabs API | ELEVENLABS_API_KEY |
| App (summarize_node/chat) | Gemini API | GEMINI_API_KEY |

## Security Requirements
- Do not commit .env or API keys
- Require GEMINI_API_KEY before Gemini LLM use
- Require ELEVENLABS_API_KEY before ElevenLabs transcription
- No persistent storage for transcripts/summaries (session_state only)

## Security Checklist
Keys in repo: fail
Env vars required: pass
External API auth: pass
Persistent transcript storage: pass
FFmpeg dependency documented: pass