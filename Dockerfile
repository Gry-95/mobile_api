FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x wait-for-it.sh entrypoint.sh entrypoint_daphne.sh

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]