# Base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy application files to the container
COPY . /app

# Install required dependencies
RUN pip install --no-cache-dir -r requirments.txt

# Expose the necessary port
EXPOSE 8777

# Copy the Scores.txt file
COPY Scores.txt /Scores.txt

# Command to run the Flask app
CMD ["python", "MainScores.py"]
