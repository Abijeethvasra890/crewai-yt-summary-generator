__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from crew import execute_summary
from tools import yt_tool
from agents import content_writer  # Import agents

def main():
    # App title and description
    st.title("YouTube Video Summary Generator")
    st.markdown("""
        **Generate summaries from YouTube videos.**  
        Provide a YouTube video URL and a topic to focus the summary on.
    """)

    # Input fields
    yt_url = st.text_input("YouTube Video URL", help="Enter the YouTube video URL")
    groq_api_key = st.text_input("Groq API Key", type="password", help="Enter your Groq API key")

    # Action button
    if st.button("Generate Summary"):
        if not yt_url or not groq_api_key:
            st.error("All fields are required.")
        else:
            content_writer.llm.api_key = groq_api_key  # Set Groq API key dynamically
            # Extract video transcript
            st.info("Extracting YouTube video transcript...")
            #transcript = yt_tool(yt_url)
            transcript = yt_tool._run(yt_url)

            if "Error" in transcript:
                st.error(transcript)
            else:
                st.success("Video transcript extracted successfully!")
                
                # Execute Crew process
                st.info("Generating summary... This may take a moment.")
                result = execute_summary(transcript)

                if "Error" in result:
                    st.error(result)
                else:
                    st.success("Summary generated successfully!")
                    st.markdown("### Generated Summary:")
                    st.write(result)

if __name__ == "__main__":
    main()
