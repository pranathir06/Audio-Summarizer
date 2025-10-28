from src.audiosummarizer.state.audio_state import AudioAnalysisState
from src.audiosummarizer.LLMS.geminillm import GeminiLLM

def summarize_node(state: AudioAnalysisState):
    """Summarize the transcript using Gemini LLM"""
    
    # Initialize Gemini LLM and create a simple summarization prompt
    llm = GeminiLLM()
    model = llm.get_llm()
    
    # Create a summarization prompt
    prompt = f"""
    
        You are an expert customer support analyst. You will receive the transcript of a customer call. 
        Your task is to analyze the transcript and provide a structured summary in the following format:

        1. **Customer Issue:** Briefly describe the problem or request the customer has.
        2. **Context / Background:** Any relevant context or history mentioned in the call.
        3. **Actions Taken / Suggested:** Any actions, solutions, or advice provided during the call.
        4. **Customer Sentiment:** Identify the customer's sentiment (e.g., frustrated, satisfied, neutral).
        5. **Key Points / Notes:** List any other important points or observations.

        Transcript: {state['transcript']}
        

        Provide the summary in **clear, concise sentences**, using bullet points where appropriate. Avoid adding information not present in the transcript.
        """
    
    # Get summary from Gemini
    response = model.invoke(prompt)
    state["summary"] = response.content if hasattr(response, 'content') else str(response)
    return state