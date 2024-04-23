# The builder image, used to build the virtual environment
FROM python:3.11.7-slim as builder

RUN apt-get update && apt-get install -y git

RUN pip install poetry==1.8.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

# The runtime image, used to just run the code provided its virtual environment
FROM python:3.11.7-slim as runtime

RUN useradd -m -u 1000 user

USER user

#ENV HOME=/home/user \
#    PATH="/home/user/.local/bin:$PATH" \
#    VIRTUAL_ENV=/app/.venv \
#    LISTEN_PORT=8000 \
#    HOST=0.0.0.0

ENV PATH="/app/.venv/bin:$PATH" \
    VIRTUAL_ENV=/app/.venv \
    LISTEN_PORT=8000 \
    HOST=0.0.0.0

WORKDIR $HOME/app

COPY --from=builder --chown=user ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY --chown=user ./app ./app
COPY --chown=user .env ./app/ 
COPY --chown=user ./.chainlit ./.chainlit
COPY --chown=user chainlit.md ./

EXPOSE $LISTEN_PORT

RUN echo "PATH=$PATH"


CMD ["chainlit", "run", "app/chatbot.py"]