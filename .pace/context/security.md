## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| GEMINI_API_KEY | Environment variable | python-dotenv loads from env; not in repo |
| ELEVENLABS_API_KEY | Environment variable | python-dotenv loads from env; not in repo |
| Transcripts | Streamlit session_state | In-memory only; no persistent store in code |
| Summaries | Streamlit session_state | In-memory only; no persistent store in code |
| ElevenLabs token usage | ~/.elevenlabs_token_usage.json | Local user home file |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| Streamlit app | Gemini API (Google) | API key via GEMINI_API_KEY |
| Streamlit app | ElevenLabs API | API key via ELEVENLABS_API_KEY |

## Security Requirements
- Do not commit .env files or API keys (AGENTS.md)
- Require GEMINI_API_KEY before LLM calls (GeminiLLM)
- Require ELEVENLABS_API_KEY before transcription (transcribe_node)
- Do not persist transcripts/summaries beyond session_state (AGENTS.md)
- ffmpeg must be installed separately for video processing

## Security Checklist
- API keys stored only in env vars: pass
- No auth/user management implemented: pass
- Persistent transcript storage present: fail
- Token usage file stored in user home: pass
- External calls gated by API keys: pass
