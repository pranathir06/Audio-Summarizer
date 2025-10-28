import streamlit as st
from src.audiosummarizer.ui.streamlitui.loadui import LoadStreamlitUI
from src.audiosummarizer.LLMS.geminillm import GeminiLLM
from src.audiosummarizer.graph.audio_graph import AudioGraphBuilder
from src.audiosummarizer.ui.streamlitui.display_result import DisplayResultStreamlit
import tempfile
import os

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.
    """

    # Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    
    # Check if audio file is uploaded and process button is clicked
    audio_file = user_input.get("audio_file")
    process_clicked = user_input.get("process_clicked", False)
    
    # If process button was clicked, always process (even if results exist)
    if audio_file is not None and process_clicked:
        # Process button was clicked - always process
        _process_audio_file(audio_file)
    elif "audio_result" in st.session_state:
        # Show cached results if available
        st.success("✅ Showing cached results")
        display_result = DisplayResultStreamlit(
            usecase="Audio Summarizer",
            audio_result=st.session_state["audio_result"]
        )
        display_result.display_result_on_ui()
    elif audio_file is not None:
        # File uploaded but not processed yet
        st.info("👆 Click the 'Process Audio File' button to start processing")
    else:
        st.warning("⚠️ Please upload an audio file to proceed")

def _process_audio_file(audio_file):
    """Process the uploaded audio file and display the LLM output"""
    try:
        # Check if we've already processed this file
        file_key = f"processed_{audio_file.name}"
        """if file_key in st.session_state:
            st.info("📄 Already processed this file")
            return"""
        
        # Show processing status
        with st.spinner("🔄 Processing audio file..."):
            # Save uploaded file to temporary location
            with tempfile.NamedTemporaryFile(delete=False, suffix=f".{audio_file.name.split('.')[-1]}") as tmp_file:
                tmp_file.write(audio_file.getvalue())
                temp_audio_path = tmp_file.name

            # Initialize LLM
            try:
                llm = GeminiLLM()
                model = llm.get_llm()
            except Exception as e:
                st.error(f"❌ Failed to initialize LLM: {e}")
                st.info("💡 Make sure to set your GEMINI_API_KEY environment variable")
                return

            # Initialize and run the audio processing graph
            graph_builder = AudioGraphBuilder(model)
            graph = graph_builder.setup_graph("Audio Summarizer")
            
            # Create initial state with audio file path
            initial_state = {
                "audio_path": temp_audio_path,
                "transcript": None,
                "summary": None
            }
            
            # Run the graph
            result = graph.invoke(initial_state)
            
            # Keep audio_path in result for chat to reuse
            result["audio_path"] = temp_audio_path
            
            # Store results in session state
            st.session_state["audio_result"] = result
            st.session_state[file_key] = True  # Mark as processed
            
            # Display results using DisplayResultStreamlit
            display_result = DisplayResultStreamlit(
                usecase="Audio Summarizer",
                audio_result=result
            )
            display_result.display_result_on_ui()
            
            # Note: Don't delete temp file yet - chat needs it for graph re-execution
            
    except Exception as e:
        st.error(f"❌ Error processing audio file: {e}")
        st.exception(e)
