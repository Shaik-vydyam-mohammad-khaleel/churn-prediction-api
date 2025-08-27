# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Expose port (Cloud Run expects 8080)
EXPOSE 8080

# Command to run the app
CMD ["python", "app.py"]

