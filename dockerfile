FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY aceest_fitness/ aceest_fitness/

ENV FLASK_APP=aceest_fitness.app:app

EXPOSE 5000

# Run with Gunicorn (more stable than flask run)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "aceest_fitness.app:app"]
