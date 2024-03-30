from uvicorn import run

from configs import app_config


if __name__ == "__main__":
    run(
        app="app.app:app",
        host=app_config.APP_HOST,
        port=app_config.APP_PORT,
        reload=True,
    )
