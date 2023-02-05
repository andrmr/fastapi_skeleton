FROM python:3.11.1-slim-bullseye

# update, upgrade
RUN apt-get update && apt-get -y upgrade
RUN python -m pip install -U pip

# install requirements
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# switch to non-root user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# install app
COPY app .

# run app
ENV UVICORN_PORT 1080
CMD uvicorn main:app --proxy-headers --host "0.0.0.0" --port $UVICORN_PORT
