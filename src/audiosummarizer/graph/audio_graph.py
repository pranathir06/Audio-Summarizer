from langgraph.graph import StateGraph, START, END
from src.audiosummarizer.state.audio_state import AudioAnalysisState
from src.audiosummarizer.nodes.audio_file_node import AudioFileNode
from src.audiosummarizer.nodes.transcribe_node import transcribe_node
from src.audiosummarizer.nodes.summarize_node import summarize_node


class AudioGraphBuilder:
    def __init__(self, llm_model):
        self.llm = llm_model
        self.graph_builder = StateGraph(AudioAnalysisState)

    def audio_summarizer_build_graph(self):
        """
        Builds an audio summarization graph using LangGraph.
        The flow is: START -> audio_file -> transcribe -> summarize -> END
        Note: Chat is handled directly in the UI, not in the graph
        """
        # Node to handle audio file input
        self.graph_builder.add_node("audio_file", AudioFileNode().process)

        # Node for ElevenLabs transcription
        self.graph_builder.add_node("transcribe", transcribe_node)

        # Node for Gemini summarization
        self.graph_builder.add_node("summarize", summarize_node)

        # Connect the nodes
        self.graph_builder.add_edge(START, "audio_file")
        self.graph_builder.add_edge("audio_file", "transcribe")
        self.graph_builder.add_edge("transcribe", "summarize")
        self.graph_builder.add_edge("summarize", END)

    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Audio Summarizer":
            self.audio_summarizer_build_graph()

        return self.graph_builder.compile()
