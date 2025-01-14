FROM python:3.13.1-slim

EXPOSE 4000

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && \
    pip install poetry

RUN poetry config virtualenvs.create true && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-root

CMD ["poetry", "run", "litellm", "--config", "examples/proxy/config.yaml", "--detailed_debug"] 
