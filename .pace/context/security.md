## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| GEMINI_API_KEY | Environment variable | Required at runtime; not in repo |
| ELEVENLABS_API_KEY | Environment variable | Required at runtime; not in repo |
| Audio files | Temp files on disk | Stored in OS temp; deleted after processing (video extraction) |
| Transcript/Summary | Streamlit session_state | In-memory per session |
| Token usage | ~/.elevenlabs_token_usage.json | Local file in user home |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| UI (Streamlit) | Gemini API via langchain-google-genai | API key in env |
| UI (Streamlit) | ElevenLabs speech_to_text | API key in env |

## Security Requirements
- Do not commit .env or API keys (AGENTS.md)
- Require GEMINI_API_KEY before GeminiLLM init (GeminiLLM)
- Require ELEVENLABS_API_KEY before transcription (transcribe_node)
- No persistent storage for transcripts/summaries beyond session_state (AGENTS.md)

## Security Checklist
API keys stored only in env: pass
Transcript persistence disabled: pass
Token usage file limited to local home dir: pass
ffmpeg dependency acknowledged for video processing: pass
