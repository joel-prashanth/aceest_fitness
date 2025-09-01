# Use official lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first (leveraging Docker cache)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY aceest_fitness/ aceest_fitness/
COPY pytest.ini .
COPY .pre-commit-config.yaml .
COPY tests/ tests/

# Expose Flask default port
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run"]
