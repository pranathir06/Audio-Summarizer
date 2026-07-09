## CI/CD
| Trigger | Workflow | Jobs |
|---|---|---|
| n/a | n/a | n/a |

## Environment Variables
| Name | Required | Purpose |
|---|---|---|
| GEMINI_API_KEY | Yes | Gemini LLM access |
| ELEVENLABS_API_KEY | Yes | ElevenLabs transcription |
| GEMINI_MODEL | No | Override Gemini model (default gemini-2.5-flash) |

## Local Dev
1. pip install -r requirements.txt
2. streamlit run app.py

## Deployment
Deploy: Streamlit run (app.py) or devcontainer postAttachCommand runs streamlit run app.py
