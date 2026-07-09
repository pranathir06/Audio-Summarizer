---
language: python
package_manager: pip
test_runner: pytest
test_command: "n/a"
test_file_pattern: "n/a"
require_tests: false
---
## Module Map
| Directory | Language | Purpose |
|---|---|---|
| . | Python | Streamlit entry point and repo configs |
| src/audiosummarizer | Python | Core audio summarizer package |
| src/audiosummarizer/LLMS | Python | LLM client setup (Gemini) |
| src/audiosummarizer/graph | Python | LangGraph workflow builder |
| src/audiosummarizer/nodes | Python | Graph nodes for file, transcription, summary |
| src/audiosummarizer/state | Python | Typed state schema |
| src/audiosummarizer/ui | Python | Streamlit UI configuration |
| src/audiosummarizer/ui/streamlitui | Python | Streamlit components and views |
| src/audiosummarizer/utils | Python | Token usage tracking |
## Tech Stack
| Component | Technology |
|---|---|
| UI | Streamlit |
| Orchestration | LangGraph (langgraph) |
| LLM | Google Gemini via langchain-google-genai |
| Transcription | ElevenLabs speech_to_text |
| Media | moviepy, mutagen, ffmpeg (external) |
| Env | python-dotenv |
## System Architecture
| Step | Component | Interaction |
|---|---|---|
| 1 | Streamlit UI | Upload audio/video, trigger processing |
| 2 | AudioGraphBuilder | Builds StateGraph with audio_file → transcribe → summarize |
| 3 | transcribe_node | Calls ElevenLabs speech_to_text, formats transcript |
| 4 | summarize_node | Calls Gemini LLM to generate structured summary |
| 5 | DisplayResultStreamlit | Shows transcript/summary and chat interface |
| 6 | ChatInterface | Uses Gemini LLM with stored transcript/summary |
## Key Interfaces & Contracts
| Interface | Location | Contract |
|---|---|---|
| AudioAnalysisState | src/audiosummarizer/state/audio_state.py | audio_path, transcript, summary, audio_duration_seconds |
| Graph entry | src/audiosummarizer/graph/audio_graph.py | START→audio_file→transcribe→summarize→END |
| LLM config | src/audiosummarizer/LLMS/geminillm.py | GEMINI_API_KEY required; GEMINI_MODEL optional |
| UI config | src/audiosummarizer/ui/uiconfigfile.ini | PAGE_TITLE, LLM_OPTIONS, USECASE_OPTIONS |
## Coding Conventions
| Rule | Source |
|---|---|
| UI logic stays in ui/; graph logic in graph/ and nodes/ | AGENTS.md |
| Use AudioAnalysisState fields exactly as defined | AGENTS.md |
| Require GEMINI_API_KEY and ELEVENLABS_API_KEY before API calls | AGENTS.md |
| Store transcripts/summaries only in st.session_state | AGENTS.md |
| Add try/except error handling in Streamlit flows | AGENTS.md |
## Test Patterns
| Item | Details |
|---|---|
| Test framework | None configured |
| Test command | n/a |
| Notes | AGENTS.md indicates tests not applicable |
