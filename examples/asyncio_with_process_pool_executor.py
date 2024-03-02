import asyncio
from concurrent.futures import ProcessPoolExecutor

# A CPU-bound operation
def cpu_intensive_task():
    print("Starting CPU-intensive task")
    # Simulate a CPU-bound task
    result = sum(i * i for i in range(10**7))
    print("CPU-intensive task completed")
    return result

async def main():
    # Create a ProcessPoolExecutor
    with ProcessPoolExecutor() as executor:
        loop = asyncio.get_running_loop()
        # Run the CPU-bound task in the executor
        result = await loop.run_in_executor(executor, cpu_intensive_task)
        print(f"CPU-bound task completed with result: {result}")

asyncio.run(main())
