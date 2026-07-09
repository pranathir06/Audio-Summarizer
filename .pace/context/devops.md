## CI/CD
| Trigger | Workflow | Jobs |
|---|---|---|
| None detected | None | None |

## Environment Variables
| Name | Required | Purpose |
|---|---|---|
| GEMINI_API_KEY | Yes | Authenticate Gemini LLM |
| GEMINI_MODEL | No | Select Gemini model (default gemini-2.5-flash) |
| ELEVENLABS_API_KEY | Yes | Authenticate ElevenLabs transcription |

## Local Dev
1. pip install -r requirements.txt
2. export GEMINI_API_KEY=...; export ELEVENLABS_API_KEY=...
3. streamlit run app.py

## Deployment
Deploy: Manual Streamlit run (app.py) or devcontainer postAttachCommand