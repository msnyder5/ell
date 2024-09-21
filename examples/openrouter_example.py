import asyncio
import logging

import ell
from ell.models.openrouter import get_client

# Configure logging to display WARNING and above messages
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@ell.simple(model="meta-llama/llama-3.1-8b-instruct")
def hello(name: str) -> str:
    """Generate a warm greeting for a provided name."""
    return f"Generate a warm greeting for {name}"

async def hello_async(name: str) -> str:
    return hello(name)


def sync_main():
    """Synchronous version of greeting generation."""
    try:
        # Get the OpenRouter client
        client = get_client()
        logger.info(f"Successfully obtained OpenRouter client: {type(client).__name__}")

        # Call the hello function
        greeting = hello("Sam Altman")
        print(f"Sync Greeting: {greeting}")

    except Exception as e:
        logger.error(f"An error occurred in sync_main: {e}")

async def async_main():
    """Asynchronous version of greeting generation."""
    try:
        # Get the OpenRouter client
        client = get_client()
        logger.info(f"Successfully obtained OpenRouter client: {type(client).__name__}")

        # Call the hello function asynchronously
        greeting = await hello_async("Sam Altman")
        print(f"Async Greeting: {greeting}")

        # Allow time for any background tasks to complete (if needed)
        await asyncio.sleep(2)

    except Exception as e:
        logger.error(f"An error occurred in async_main: {e}")

if __name__ == "__main__":
    # Run the synchronous function
    sync_main()

    # Run the asynchronous function
    asyncio.run(async_main())
