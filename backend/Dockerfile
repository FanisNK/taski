FROM python:3.12-slim

WORKDIR /app

RUN pip install --upgrade pip setuptools

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi"]
