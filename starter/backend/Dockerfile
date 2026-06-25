FROM public.ecr.aws/docker/library/python:3.10-alpine

ENV FLASK_RUN_HOST=0.0.0.0

# ✅ CRITICAL: run from /app
WORKDIR /app

RUN adduser -u 1000 -D app

RUN apk update && \
  apk add \
  pcre \
  pcre-dev \
  build-base \
  gcc \
  linux-headers \
  openssl \
  libffi-dev \
  && pip install pipenv

# ✅ install dependencies
COPY Pipfile* /app/
RUN cd /app && pipenv install --system --deploy

# ✅ KEEP STRUCTURE: copy everything INCLUDING starter/
COPY .. /app

# ✅ CRITICAL: expose starter as module root
ENV PYTHONPATH=/app

USER app

EXPOSE 5000

# ✅ FINAL FIX (THIS IS WHAT YOU WERE MISSING)
CMD ["python", "-m", "starter.backend"]
