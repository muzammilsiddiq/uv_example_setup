import os

import requests
import streamlit as st

# Set via docker-compose.yml. Falls back to localhost for running outside Docker.
BACKEND_URL = os.environ.get("APP_BACKEND_URL", "http://localhost:8000")


def main() -> None:
    st.set_page_config(page_title="uv + Docker Compose Example")
    st.title("Streamlit frontend -> FastAPI backend")
    st.caption(f"Backend URL: {BACKEND_URL}")

    if st.button("Call backend root endpoint (/)"):
        try:
            response = requests.get(BACKEND_URL, timeout=5)
            response.raise_for_status()
            st.json(response.json())
        except requests.RequestException as exc:
            st.error(f"Could not reach backend: {exc}")

    if st.button("Call backend health endpoint (/healthz)"):
        try:
            response = requests.get(f"{BACKEND_URL}/healthz", timeout=5)
            response.raise_for_status()
            st.json(response.json())
        except requests.RequestException as exc:
            st.error(f"Could not reach backend: {exc}")


def run() -> None:
    """Entry point for the `serve-frontend` console script."""
    import sys

    from streamlit.web import cli as stcli

    sys.argv = [
        "streamlit",
        "run",
        __file__,
        "--server.port=8501",
        "--server.address=0.0.0.0",
    ]
    sys.exit(stcli.main())


if __name__ == "__main__":
    main()
