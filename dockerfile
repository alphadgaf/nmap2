FROM python:3.13-slim

# Install Nmap
RUN apt-get update && apt-get install -y nmap && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Render’s Docker web services listen on 10000 by convention
EXPOSE 10000

# Start your bot (Flask runs inside bot.py)
CMD ["python", "bot.py"]
