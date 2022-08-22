# FROM python:3.11.0rc1-slim-bullseye
FROM python:3.10-slim@sha256:e266c9c8a5a11df3183675b60a0a61b8cf22a9eeb4b229af86dcd2daf0f4475a
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
ENTRYPOINT flask run -h '0.0.0.0' -p 5000