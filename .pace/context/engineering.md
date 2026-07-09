---
language: python
package_manager: pip
test_runner: none
test_command: "n/a"
test_file_pattern: "n/a"
require_tests: false
---
## Module Map
| Directory | Language | Purpose |
|---|---|---|
| . | Python | Streamlit entrypoint and repo docs |
| src/audiosummarizer | Python | Audio summarization app package |
| src/audiosummarizer/LLMS | Python | Gemini LLM wrapper |
| src/audiosummarizer/graph | Python | LangGraph builder |
| src/audiosummarizer/nodes | Python | Graph nodes (audio, transcribe, summarize) |
| src/audiosummarizer/state | Python | Typed state schema |
| src/audiosummarizer/ui | Python | UI config + Streamlit UI modules |
| src/audiosummarizer/ui/streamlitui | Python | Streamlit components (chat, display) |
| src/audiosummarizer/utils | Python | Token usage tracking |

## Tech Stack
| Component | Technology |
|---|---|
| UI | Streamlit |
| Orchestration | LangGraph |
| LLM | Google Gemini via langchain-google-genai |
| Transcription | ElevenLabs speech_to_text |
| Media processing | moviepy, mutagen, ffmpeg |
| Env config | python-dotenv |

## System Architecture
| Flow Step | Component | Details |
|---|---|---|
| Entry | app.py | Calls load_langgraph_agenticai_app() |
| UI | LoadStreamlitUI | Upload file, token usage, process button |
| Graph | AudioGraphBuilder | START→audio_file→transcribe→summarize→END |
| Transcription | transcribe_node | ElevenLabs diarized transcription; video audio extraction |
| Summarization | summarize_node | Gemini prompt for structured summary |
| Chat | ChatInterface | Q&A over transcript+summary via Gemini |
| Persistence | TokenTracker | ~/.elevenlabs_token_usage.json usage tracking |

## Key Interfaces & Contracts
| Interface | Location | Contract |
|---|---|---|
| Streamlit entry | app.py | run: streamlit run app.py |
| LangGraph state | audio_state.AudioAnalysisState | audio_path:str, transcript:Optional[str], summary:Optional[str], audio_duration_seconds:Optional[float] |
| Env vars | GeminiLLM, transcribe_node | GEMINI_API_KEY, GEMINI_MODEL (optional), ELEVENLABS_API_KEY |
| UI config | ui/uiconfigfile.ini | PAGE_TITLE, LLM_OPTIONS, USECASE_OPTIONS, GROQ_MODEL_OPTIONS |
| LangGraph config | langgraph.json | graphs.agent = ./main.py:graph |

## Coding Conventions
| Area | Convention |
|---|---|
| UI errors | Streamlit st.error/st.warning with try/except (main.py, loadui.py) |
| State handling | Use dict access for AudioAnalysisState in nodes |
| API keys | Validate GEMINI_API_KEY at GeminiLLM init; ELEVENLABS_API_KEY in transcribe_node |
| Token tracking | TokenTracker JSON file in user home |

## Test Patterns
| Aspect | Details |
|---|---|
| Tests present | No test infrastructure (AGENTS.md: "How to Run Tests n/a") |
| Expected | Manual UI run via Streamlit |
