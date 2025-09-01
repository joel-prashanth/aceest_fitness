FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY aceest_fitness/ aceest_fitness/

# Set environment variables so Flask finds the app
ENV FLASK_APP=aceest_fitness.app:app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

EXPOSE 5000

# Run flask app
CMD ["flask", "run"]
