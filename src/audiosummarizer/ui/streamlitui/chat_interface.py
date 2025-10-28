import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from src.audiosummarizer.LLMS.geminillm import GeminiLLM


class ChatInterface:
    def __init__(self, audio_result_key="audio_result"):
        """
        Initialize chat interface that uses pre-processed audio data from session state
        
        Args:
            audio_result_key: Key in session state where audio results are stored
        """
        self.audio_result_key = audio_result_key
        
        # Initialize chat history in session state
        if "chat_messages" not in st.session_state:
            st.session_state.chat_messages = []
    
    def display_chat(self):
        """Display the chat interface and handle questions through graph execution"""
        st.subheader("💬 Ask Questions About the Audio")
        
        # Display chat history
        for message in st.session_state.chat_messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Accept user input
        if user_question := st.chat_input("Ask anything about the audio..."):
            # Check if audio data is available
            if self.audio_result_key not in st.session_state:
                st.error("No audio data available. Please process an audio file first.")
                return
            
            # Add user message to chat
            st.session_state.chat_messages.append({
                "role": "user",
                "content": user_question
            })
            
            # Display user message
            with st.chat_message("user"):
                st.markdown(user_question)
            
            # Get AI response (no graph execution)
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = self._get_answer_via_graph(user_question)
                    st.markdown(response)
            
            # Add AI message to chat
            st.session_state.chat_messages.append({
                "role": "assistant",
                "content": response
            })
    
    def _get_answer_via_graph(self, question):
        """Get answer directly without re-running the graph"""
        # Get the existing audio result
        audio_result = st.session_state.get("audio_result")
        
        if not audio_result:
            return "No audio data available."
        
        # Get transcript and summary from existing results
        transcript = audio_result.get("transcript", "")
        summary = audio_result.get("summary", "")
        
        # Handle transcript if it's an object with text attribute
        transcript_text = transcript.text if hasattr(transcript, 'text') else str(transcript)
        
        try:
            # Initialize LLM
            from src.audiosummarizer.LLMS.geminillm import GeminiLLM
            
            llm = GeminiLLM()
            model = llm.get_llm()
            
            # Build prompt
            prompt = f"""You are an AI assistant that answers questions about customer call transcripts.

Context Information:
1. Audio Transcript: {transcript_text}
2. Summary: {summary}

User Question: {question}

Instructions:
- Answer the question based on the transcript and summary provided
- If the question cannot be answered from the available information, say so clearly
- Be concise and specific in your answers
- Reference specific parts of the conversation when relevant
- If asked about sentiment, emotions, or tone, analyze the language used in the transcript
- If asked about specific topics, facts, or actions, provide exact quotes or paraphrases from the transcript

Provide your answer:"""

            # Get response from LLM
            response = model.invoke(prompt)
            answer = response.content if hasattr(response, 'content') else str(response)
            
            return answer
            
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"
    
    def clear_chat(self):
        """Clear chat history"""
        if st.button("🗑️ Clear Chat History"):
            st.session_state.chat_messages = []
            st.rerun()

