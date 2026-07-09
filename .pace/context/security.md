## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| GEMINI_API_KEY | Environment variable | Not committed; loaded via dotenv |
| ELEVENLABS_API_KEY | Environment variable | Not committed; loaded via dotenv |
| Audio files (uploads) | Temp files on local disk | Temporary files; deletion after processing for video extract; audio file retained for chat |
| Transcripts/Summaries | Streamlit session_state | In-memory per session only |
| Token usage data | ~/.elevenlabs_token_usage.json | Local user file; no encryption specified |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| Streamlit UI | Gemini API (langchain-google-genai) | API key (GEMINI_API_KEY) |
| Streamlit UI | ElevenLabs API | API key (ELEVENLABS_API_KEY) |
| Transcribe node | ffmpeg/moviepy | Local process execution |

## Security Requirements
- Do not commit .env files or API keys (AGENTS.md)
- Require GEMINI_API_KEY and ELEVENLABS_API_KEY before API calls
- Avoid persistent storage of transcripts/summaries beyond session_state

## Security Checklist
API keys stored in env only: pass
Persistent transcript storage avoided: pass
User auth present: fail
Input file type validation present: pass
