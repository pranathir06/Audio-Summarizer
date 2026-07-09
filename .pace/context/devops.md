## CI/CD
| Trigger | Workflow | Jobs |
|---|---|---|
| None | None | None |

## Environment Variables
| Name | Required | Purpose |
|---|---|---|
| GEMINI_API_KEY | Yes | Google Gemini API access |
| ELEVENLABS_API_KEY | Yes | ElevenLabs transcription |
| GEMINI_MODEL | No | Override Gemini model name |

## Local Dev
1. pip install -r requirements.txt
2. export GEMINI_API_KEY=... && export ELEVENLABS_API_KEY=...
3. streamlit run app.py

## Deployment
Deploy: Streamlit app run via `streamlit run app.py` (devcontainer auto-runs)