import streamlit as st
import re
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json
from src.audiosummarizer.ui.streamlitui.chat_interface import ChatInterface


class DisplayResultStreamlit:
    def __init__(self, usecase=None, graph=None, user_message=None, audio_result=None):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message
        self.audio_result = audio_result

    def display_result_on_ui(self):
        """Display results based on the use case"""
        
        if self.usecase == "Audio Summarizer":
            self._display_audio_result()
        else:
            st.error(f"Unknown use case: {self.usecase}")

    

    def _display_audio_result(self):
        """Display audio processing results"""
        if not self.audio_result:
            st.error("No audio processing results to display")
            return

        # Store results in session state for chat to access
        st.session_state["audio_result"] = self.audio_result

        st.success("✅ Audio processing completed!")
        
        # Display transcript in a collapsible box
        if self.audio_result.get("transcript"):
            transcript_text = self.audio_result["transcript"].text if hasattr(self.audio_result["transcript"], 'text') else str(self.audio_result["transcript"])
            
            with st.expander("📝 Transcript", expanded=False):
                st.text_area(
                    "Full transcription of the audio file:", 
                    transcript_text, 
                    height=300, 
                    disabled=True,
                    label_visibility="collapsed",
                    help="This is the transcribed text from your audio file"
                )
        else:
            st.warning("⚠️ No transcript available")
        
        # Display summary in a collapsible box
        

        if self.audio_result.get("summary"):
            summary = self.audio_result["summary"]

            # Apply basic formatting: bold headers, emojis, etc.
            summary = re.sub(r"\*\*Customer Issue:\*\*", "🧾 **Customer Issue:**", summary)
            summary = re.sub(r"\*\*Context / Background:\*\*", "📖 **Context / Background:**", summary)
            summary = re.sub(r"\*\*Actions Taken / Suggested:\*\*", "⚙️ **Actions Taken / Suggested:**", summary)
            summary = re.sub(r"\*\*Customer Sentiment:\*\*", "💬 **Customer Sentiment:**", summary)
            summary = re.sub(r"\*\*Key Points / Notes:\*\*", "📌 **Key Points / Notes:**", summary)

            st.markdown("## 📋 Audio Summary")
            st.markdown(
                f"""
                <div style="
                    #background-color:#F7F9FC;
                    padding:20px;
                    border-radius:15px;
                    border:1px solid #E3E6EA;
                    font-size:16px;
                    line-height:1.6;
                ">
                {summary}
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.warning("⚠️ No summary generated yet.")


        st.divider()
        
        # Display chat interface - it will read from session state
        chat = ChatInterface()
        chat.display_chat()

    """def _download_summary(self):
        Provide download option for the summary
        if self.audio_result.get("summary"):
            summary_text = self.audio_result["summary"]
            st.download_button(
                label="📥 Download Summary as Text",
                data=summary_text,
                file_name="audio_summary.txt",
                mime="text/plain"
            )"""
