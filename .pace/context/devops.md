## CI/CD
| Trigger | Workflow | Jobs |
|---|---|---|
| None | .github/workflows not present | n/a |

## Environment Variables
| Name | Required | Purpose |
|---|---|---|
| GEMINI_API_KEY | Yes | Gemini LLM access (geminillm.py) |
| ELEVENLABS_API_KEY | Yes | ElevenLabs transcription (transcribe_node.py) |
| GEMINI_MODEL | No | Select Gemini model (default gemini-2.5-flash) |

## Local Dev
1. pip install -r requirements.txt
2. export GEMINI_API_KEY=... && export ELEVENLABS_API_KEY=...
3. streamlit run app.py

## Deployment
Deploy: streamlit run app.py (no deployment scripts found)
