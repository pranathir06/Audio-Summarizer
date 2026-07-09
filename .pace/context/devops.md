## CI/CD
| Trigger | Workflow | Jobs |
|---|---|---|
| None | None | None |

## Environment Variables
| Name | Required | Purpose |
|---|---|---|
| GEMINI_API_KEY | Yes | Gemini LLM access |
| GEMINI_MODEL | No | Select Gemini model (default gemini-2.5-flash) |
| ELEVENLABS_API_KEY | Yes | ElevenLabs transcription access |

## Local Dev
1. pip install -r requirements.txt
2. export GEMINI_API_KEY=...  (and ELEVENLABS_API_KEY=...)
3. streamlit run app.py

## Deployment
Deploy: Streamlit run app.py (no deploy config found)
