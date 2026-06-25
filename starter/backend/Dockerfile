FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  python3-dev \
  libpcre2-dev \
  libcrypt-dev \
  libssl-dev \
  && rm -rf /var/lib/apt/lists/*

RUN useradd -u 1000 -m app

RUN pip install pipenv

COPY Pipfile* /app/
RUN pipenv install --system --deploy

COPY . /app

ENV PYTHONPATH=/app

USER app

EXPOSE 5000

CMD ["python", "-c", "from starter.backend import app; app.run(host='0.0.0.0', port=5000)"]