FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install daphne
RUN pip show daphne
COPY . .
EXPOSE 8000
CMD ["daphne", "oc_lettings_site.asgi:application", "--bind", "0.0.0.0:${PORT:-8000}"]