from crewai import Crew, Process
from tasks import write_task
from agents import content_writer

# Define the Crew
crew = Crew(
    agents=[content_writer],
    tasks=[write_task],
    verbose=True
)

# Example execution
def execute_summary(transcript):
    """Executes the summary generation process."""
    try:
        result = crew.kickoff(inputs={"transcript": transcript})
        return result
    except Exception as e:
        return f"Error during execution: {str(e)}"
