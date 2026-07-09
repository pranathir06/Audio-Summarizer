## CI/CD
| Trigger | Workflow | Jobs |
|---|---|---|
| None | None | None |

## Environment Variables
| Name | Required | Purpose |
|---|---|---|
| GEMINI_API_KEY | Yes | Gemini LLM access |
| ELEVENLABS_API_KEY | Yes | ElevenLabs transcription access |
| GEMINI_MODEL | No | Override Gemini model (default gemini-2.5-flash) |

## Local Dev
1. pip install -r requirements.txt
2. export GEMINI_API_KEY=... (or set in .env)
3. export ELEVENLABS_API_KEY=...
4. streamlit run app.py

## Deployment
Deploy: Streamlit app run via `streamlit run app.py` (no deployment config found)
