# Use official Python image
FROM python:3.13-slim

# Install system dependencies
RUN apt-get update && apt-get install -y nmap && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Flask
EXPOSE 5000

# Command to run the bot
CMD ["python", "bot.py"]
