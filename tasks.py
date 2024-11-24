from crewai import Task
from agents import content_writer

# Writing Task
write_task = Task(
    description=(
        "Summarize the transcription and create a concise summary for the topic from the video based on {transcript}."
    ),
    expected_output="A well-written summary focused on the given topic from the video based on {transcript}.",
    agent=content_writer,
    async_execution=False,
)