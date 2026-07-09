## CI/CD
| Trigger | Workflow | Jobs |
|---|---|---|
| n/a | None found in .github/workflows | n/a |
## Environment Variables
| Name | Required | Purpose |
|---|---|---|
| GEMINI_API_KEY | Yes | Authenticate Gemini LLM calls |
| GEMINI_MODEL | No | Select Gemini model (default gemini-2.5-flash) |
| ELEVENLABS_API_KEY | Yes | Authenticate ElevenLabs transcription |
## Local Dev
1. pip install -r requirements.txt
2. streamlit run app.py
## Deployment
Deploy: Streamlit app (streamlit run app.py)
