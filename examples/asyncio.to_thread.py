import asyncio
import time

# A blocking I/O operation
def blocking_io_task():
    print("Starting blocking I/O task in a separate thread")
    time.sleep(2)
    print("Blocking I/O task completed")
    return "Result of blocking I/O"

async def main():
    # Offload the blocking task to a separate thread
    result = await asyncio.to_thread(blocking_io_task)
    print(f"Blocking task completed with result: {result}")

asyncio.run(main())

