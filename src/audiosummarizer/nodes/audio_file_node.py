from src.audiosummarizer.state.audio_state import AudioAnalysisState

class AudioFileNode:
    def process(self, state: AudioAnalysisState):
        # LangGraph passes state as a dictionary, so we need to access it as such
        print(f"Received audio file: {state['audio_path']}")
        return state