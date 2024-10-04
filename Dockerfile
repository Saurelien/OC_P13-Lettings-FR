FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh
EXPOSE 8000
COPY . .
CMD ["/app/start.sh"]