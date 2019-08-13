FROM python:3.11-slim as builder
ENV POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME='/usr/local' \
    PIP_NO_CACHE_DIR=on
RUN apt-get update && apt-get upgrade -y \
    curl \
    && apt-get install --no-install-recommends -y \
    && curl -sSL 'https://install.python-poetry.org' | python - \
    && poetry --version \
    # Cleaning cache:
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./poetry.lock ./pyproject.toml ./
RUN poetry version \
    && poetry install

FROM python:3.11-slim
RUN groupadd -r roleplay && \
    useradd -g roleplay -ms /bin/bash roleplay && \
    pip install poetry
USER roleplay
WORKDIR /app
# COPY --from=builder /var/cache/pypoetry /var/cache/pypoetry
COPY --from=builder --chown=roleplay:roleplay /usr/local /usr/local
COPY --chown=roleplay:roleplay ./app/ ./

CMD [ "python", "main.py"]
