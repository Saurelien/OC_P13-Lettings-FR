FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["daphne", "oc_lettings_site.asgi:application", "-p", "8000", "-b", "0.0.0.0"]