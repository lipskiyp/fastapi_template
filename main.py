from uvicorn import run

from messenger.app.configs import messenger_config


if __name__ == "__main__":
    run(
        app="messenger:messenger",
        host=messenger_config.APP_HOST,
        port=messenger_config.APP_PORT,
        reload=True,
    )
