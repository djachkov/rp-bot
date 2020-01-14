
FROM python:slim
LABEL version="0.0.1-alpha" \
    maintainer="Dmitrii Diachkov <dmitrij.djachkov@yandex.ru>" \
    description="Docker image for the Telegram-based roleplay game"

RUN groupadd -r roleplay && \
    useradd -g roleplay -ms /bin/bash roleplay && \
    pip install poetry
USER roleplay
WORKDIR /home/roleplay
COPY --chown=roleplay:roleplay . .
RUN poetry install --no-dev
CMD [ "poetry", "run", "game"]

