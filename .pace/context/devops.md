## CI/CD
| Trigger | Workflow | Jobs |
|---|---|---|
| n/a | n/a | n/a |

## Environment Variables
| Name | Required | Purpose |
|---|---|---|
| GEMINI_API_KEY | Yes | Gemini LLM auth |
| ELEVENLABS_API_KEY | Yes | ElevenLabs transcription auth |
| GEMINI_MODEL | No | Override Gemini model name |

## Local Dev
1. pip install -r requirements.txt
2. export GEMINI_API_KEY=... (or set in env)
3. export ELEVENLABS_API_KEY=...
4. streamlit run app.py

## Deployment
Deploy: Streamlit run app.py (devcontainer runs with streamlit in postAttachCommand)