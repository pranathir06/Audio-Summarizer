## CI/CD
| Trigger | Workflow | Jobs |
|---|---|---|
| n/a | n/a | n/a |

## Environment Variables
| Name | Required | Purpose |
|---|---|---|
| GEMINI_API_KEY | yes | Gemini API access |
| ELEVENLABS_API_KEY | yes | ElevenLabs transcription |
| GEMINI_MODEL | no | Override default Gemini model |

## Local Dev
1. pip install -r requirements.txt
2. export GEMINI_API_KEY=... (or set in env)
3. export ELEVENLABS_API_KEY=...
4. streamlit run app.py

## Deployment
Deploy: Streamlit app (run app.py)