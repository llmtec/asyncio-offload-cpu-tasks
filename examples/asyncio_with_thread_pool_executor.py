import asyncio
from concurrent.futures import ThreadPoolExecutor

# A blocking I/O operation
def blocking_io_task():
    # Simulate a blocking I/O operation
    print("Starting blocking I/O task")
    # Block for 2 seconds
    time.sleep(2)
    print("Blocking I/O task completed")
    return "Result of blocking I/O"

async def main():
    loop = asyncio.get_running_loop()
    # Create a ThreadPoolExecutor
    with ThreadPoolExecutor() as executor:
        # Run the blocking task in the executor
        result = await loop.run_in_executor(executor, blocking_io_task)
        print(f"Blocking task completed with result: {result}")

asyncio.run(main())
