FROM python:3.12-alpine
WORKDIR /app
COPY . .
RUN --mount=type=cache,id=custom-pip,target=/root/.cachmakee/pip pip install -r requirements.txt