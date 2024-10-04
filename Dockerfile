FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
COPY . .
COPY start.sh /usr/local/bin/start.sh
CMD ["/usr/local/bin/start.sh"]