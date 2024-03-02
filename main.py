from fastapi import FastAPI, Depends
from executor import AppExecutor

app = FastAPI()

@app.on_event("startup")
def on_startup():
    # Initialize the shared executor with 5 workers; adjust as needed
    AppExecutor.get_instance(max_workers=5, use_processes=False)
    print("Application starting, executor ready.")

@app.on_event("shutdown")
def on_shutdown():
    AppExecutor.shutdown()
    print("Application shutting down, executor shut down.")

@app.get("/")
async def read_root():
    executor = AppExecutor.get_instance()
    future = executor.submit(lambda: "Hello, World from ThreadPoolExecutor!")
    result = future.result()
    return {"message": result}
