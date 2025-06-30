FROM python:3.11-slim

WORKDIR /app

# Copy requirements first (caches better)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of bot code
COPY . .

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python", "bot.py"]
