import os
import asyncio
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search
from google.genai import types

load_dotenv()

print("✅ ADK components imported successfully.")

try:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "FALSE"
    print("✅ Gemini API key setup complete.")
except Exception as e:
    print(f"🔑 Authentication Error: Please make sure you have added 'GOOGLE_API_KEY' to your Kaggle secrets. Details: {e}")

try:
    #loading agent
    root_agent = Agent(
        name="helpful_assistant",
        model="gemini-2.5-flash-lite",
        description="A simple agent that can answer general questions.",
        instruction="You are a helpful assistant. Use Google Search for current info or if unsure.",
        tools=[google_search],
    )

    print("✅ Root Agent defined.")
except Exception as e:
    print(f"🔑 Error defining root agent: {e}")

async def main():
    runner = InMemoryRunner(agent=root_agent)
    print("✅ Runner created.")
    query = input("What do you want to know about?")
    await runner.run_debug(query)

if __name__ == "__main__":
    asyncio.run(main())

#create adk agent
#adk create sample-agent --model gemini-2.5-flash-lite --api_key $GOOGLE_API_KEY

#run adk agent
#adk web --port 8000