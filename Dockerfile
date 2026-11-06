# Multi-stage: MkDocs build (needs Cairo for social cards) → nginx static serve (Render web service).
FROM python:3.12-slim-bookworm AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    libcairo2-dev \
    libpango1.0-dev \
    libgdk-pixbuf2.0-dev \
    libffi-dev \
    shared-mime-info \
    git \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdocs build --strict

FROM nginx:1.27-alpine

# Render sets $PORT; nginx official image substitutes templates on startup.
COPY docker/nginx-default.conf.template /etc/nginx/templates/default.conf.template
ENV PORT=8080

COPY --from=builder /app/site /usr/share/nginx/html
