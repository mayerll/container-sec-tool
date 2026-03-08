
# Sample Dockerfile with intentional issues

# Using root user by default
FROM python:3.11-slim

# Using ADD instead of COPY
ADD requirements.txt /app/

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose a privileged port (example)
EXPOSE 80

# Set root user explicitly
USER root

# Default command
CMD ["python", "app.py"]
