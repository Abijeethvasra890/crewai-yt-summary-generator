from youtube_transcript_api import YouTubeTranscriptApi
from crewai.tools import BaseTool
from typing import Any


# Function to extract transcript
def extract_transcript(video_id: str) -> str:
    """Extract transcript text from a YouTube video."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry["text"] for entry in transcript])
    except Exception as e:
        return f"Error: {str(e)}"


# Tool for extracting video ID and transcript
class YouTubeTranscriptTool(BaseTool):
    name: str = "YouTube Transcript Tool"  # Add type annotations
    description: str = "Extracts the transcript of a YouTube video based on its URL."

    def _run(self, url: str) -> Any:  # Properly annotate the run method
        """Run the tool to process a YouTube URL."""
        if "v=" in url:
            video_id = url.split("v=")[1].split("&")[0]
        elif "youtu.be/" in url:
            video_id = url.split("youtu.be/")[1]
        else:
            return "Invalid YouTube URL format."
        return extract_transcript(video_id)


# Instantiate the tool
yt_tool = YouTubeTranscriptTool()
