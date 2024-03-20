def create():
    from fastapi import FastAPI
    from .routers import task, done

    api = FastAPI()

    api.include_router(task.router)
    api.include_router(done.router)

    return api