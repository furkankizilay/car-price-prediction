#See full documentation in https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
# It will expect a file at /app/main.py and will expect it to contain a variable app with your FastAPI application.
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY /app/requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY ./model /model/
COPY ./app /app
