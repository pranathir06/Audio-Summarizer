## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| GEMINI_API_KEY | Environment variable | Not stored in code; loaded via dotenv |
| ELEVENLABS_API_KEY | Environment variable | Not stored in code; loaded via dotenv |
| Audio files | Temp files created in main.py and loadui.py | Local temp storage; no encryption noted |
| Transcript/Summary | st.session_state | In-memory Streamlit session state |
| ElevenLabs token usage | ~/.elevenlabs_token_usage.json | Local file; no encryption noted |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| Streamlit app | Google Gemini API | API key (GEMINI_API_KEY) |
| Streamlit app | ElevenLabs API | API key (ELEVENLABS_API_KEY) |
| UI components | Local filesystem | None (local file access) |

## Security Requirements
- Do not commit API keys or .env files (AGENTS.md)
- Require GEMINI_API_KEY and ELEVENLABS_API_KEY before external calls
- Do not add persistent storage for transcripts/summaries (AGENTS.md)
- Preserve ffmpeg requirement for video processing

## Security Checklist
Secrets committed to repo: Pass
API keys required before LLM/transcription calls: Pass
Transcripts persisted to disk: Pass (not persisted)
Local token usage file protected/encrypted: Fail (plain JSON)