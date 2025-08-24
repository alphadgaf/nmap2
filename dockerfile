# Use Python 3.13 slim image
FROM python:3.13-slim

# Install Nmap and other dependencies
RUN apt-get update && apt-get install -y nmap && apt-get clean

# Set working directory
WORKDIR /app

# Copy all project files to the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your bot
CMD ["python", "bot.py"]
