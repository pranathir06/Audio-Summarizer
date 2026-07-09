## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| GEMINI_API_KEY | Environment variable | Not committed; read via dotenv/env |
| ELEVENLABS_API_KEY | Environment variable | Not committed; read via dotenv/env |
| Audio transcript/summary | Streamlit session state | In-memory only; no persistence |
| Token usage file | ~/.elevenlabs_token_usage.json | Local file in user home directory |
## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| Streamlit app | Gemini API (langchain-google-genai) | API key in GEMINI_API_KEY |
| Streamlit app | ElevenLabs speech_to_text | API key in ELEVENLABS_API_KEY |
## Security Requirements
- Do not commit API keys or .env files
- Require GEMINI_API_KEY before LLM calls
- Require ELEVENLABS_API_KEY before transcription
- No persistent storage for transcripts/summaries
## Security Checklist
API keys stored in env vars: pass
Transcripts persisted to disk: fail (must remain in session state)
ffmpeg required for video processing: pass
