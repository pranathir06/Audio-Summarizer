## CI/CD
| Trigger | Workflow | Jobs |
|---|---|---|
| n/a | n/a | n/a |

## Environment Variables
| Name | Required | Purpose |
|---|---|---|
| GEMINI_API_KEY | Yes | Google Gemini LLM access |
| GEMINI_MODEL | No | Override Gemini model name |
| ELEVENLABS_API_KEY | Yes | ElevenLabs transcription access |

## Local Dev
1. pip install -r requirements.txt
2. export GEMINI_API_KEY=... ELEVENLABS_API_KEY=...
3. streamlit run app.py

## Deployment
Deploy: Streamlit run app.py (no deploy config detected)