FROM python:3.8-buster@sha256:c60308189ecec21e11a8ec842393c0ba6015de05e2d7e1aeafaaeb7bd41fe115
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
ENTRYPOINT flask run -h '0.0.0.0' -p 8080