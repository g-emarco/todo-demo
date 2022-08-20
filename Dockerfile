FROM python:python:3.11-rc-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
ENTRYPOINT flask run -h '0.0.0.0' -p 5000