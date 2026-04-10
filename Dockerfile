FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends fontconfig && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Crimson Pro fonts at system level
COPY fonts/ /usr/share/fonts/truetype/crimsonpro/
RUN fc-cache -fv

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:${PORT:-5000} --workers 2 --timeout 120 app:app
