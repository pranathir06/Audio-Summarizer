## CI/CD
| Trigger | Workflow | Jobs |
|---|---|---|
| n/a | n/a | n/a |

## Environment Variables
| Name | Required | Purpose |
|---|---|---|
| GEMINI_API_KEY | Yes | Gemini LLM access |
| GEMINI_MODEL | No | Model selection (default gemini-2.5-flash) |
| ELEVENLABS_API_KEY | Yes | ElevenLabs transcription |

## Local Dev
1. pip install -r requirements.txt
2. export GEMINI_API_KEY=... (or set in .env)
3. export ELEVENLABS_API_KEY=...
4. streamlit run app.py

## Deployment
Deploy: Streamlit app run via app.py (no deployment config found)
