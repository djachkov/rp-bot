# Quickstart
From now, the app using **[poetry](https://python-poetry.org/)** as a project dependencies manager.
You can use both **poetry** or **pip** to install project dependencies.
## Installing through the poetry
Install poetry, using the official [guide](https://python-poetry.org/docs/)
Navigate to the project folder and run `poetry install`.
It will also install all development dependencies and create a virtualenv for the project.
## Installing through the pip
Navigate to the project folder and run `pip install -r requirements.txt`
If you want to use virtualenv, you must create it before using the *pip*
It recommends, to install all dev-dependencies for the local development. You can find a list of dependencies in the *pyproject.toml*
## Before the launch
You must create *.env* file in the project folder, which will contain all environment variables for the project:
```toml
TOKEN="TELEGRAM_BOT_TOKEN"
LOGGING_LEVEL="INFO|DEBUG|etc."
```
To run the app on your local environment, just start the app using:
`python app.py`

# Available commands
*/start* - initiate bot.