FROM python:3.11-slim

WORKDIR /app

# Install the required Prometheus library
RUN pip install --no-cache-dir prometheus-client

# Copy the app code
COPY app.py .

# Expose the internal metrics port
EXPOSE 8000

# Run the app
CMD ["python", "app.py"]

