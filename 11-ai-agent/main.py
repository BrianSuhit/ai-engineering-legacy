import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def get_course_schedule():
    """Returns the schedule for the first four-month period at TUDAI."""
    return {
        "Monday": "Computational Mathematics Workshop: 18:00 to 21:00",
        "Tuesday": "Programming 1: 15:00 to 18:00 - Computational Mathematics Workshop: 18:00 to 21:00",
        "Wednesday": "Programming 1: 15:00 to 17:00",
        "Thursday": "Programming 1: 15:00 to 18:00",
        "Friday": "English: 18:00 to 21:00",
        "Total_weekly_hours" : "20 hours per week"
    }

def get_holidays():
    """Returns a list of Argentine holidays for the first half of the year."""
    return {
        "Wednesday, January 1": "New Year",
        "Monday, February 16": "Carnival",
        "Tuesday, February 17": "Carnival",
        "Tuesday, March 24": "National Day of Memory for Truth and Justice",
        "Thursday, April 2": "Day of the Veteran and Fallen in the Malvinas War and Holy Thursday",
        "Friday, April 3": "Good Friday",
        "Saturday, April 4": "Anniversary of the city of Tandil",
        "Friday, May 1": "Labor Day",
        "Monday, May 25": "May Revolution Day",
        "Monday, June 15": "Day of the Passing into Immortality of General Martín Miguel de Güemes",
        "Saturday, June 20": "Day of the Passing into Immortality of General Manuel Belgrano"
    }

# A list of tools that the generative model can use.
available_tools = [get_course_schedule, get_holidays]

def start_agent():
    """Initializes and runs the schedule agent chat session."""
    print("🤖 Schedule Agent online. Ask me anything.")
    
    # Create a new chat session with the model, configured to use the available tools.
    chat = client.chats.create(
        model="gemini-3.1-flash-lite-preview",
        config={
            "tools": available_tools,
            "system_instruction": "You are Brian's assistant. Use the schedule and holidays tools to answer accurately. If the information is not sufficient, say that you don't know."
        }
    )

    # Main loop to handle user interaction.
    while True:
        user_input = input("\n👤 Brian: ")
        
        # Exit condition for the chat loop.
        if user_input.lower() in ["quit", "bye", "exit"]:
            break

        # Send the user's message to the model and get the response.
        # The agent will reason and decide whether to use the provided tool.
        response = chat.send_message(user_input)
        
        print(f"\n🤖 Agent: {response.text}")

# Entry point of the script.
if __name__ == "__main__":
    start_agent()