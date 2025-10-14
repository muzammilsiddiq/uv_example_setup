from fastapi import FastAPI

app = FastAPI(title="UV + Docker + FastAPI Example")


@app.get("/")
def read_root() -> dict:
    return {"message": "Hello from uv + Docker + FastAPI"}


@app.get("/healthz")
def health_check() -> dict:
    return {"status": "ok"}


def run() -> None:
    """Entry point for the `serve` console script."""
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info",
    )