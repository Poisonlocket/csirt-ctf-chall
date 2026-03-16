FROM python:3.11-slim

# create app directory
WORKDIR /app

# install dependencies
RUN pip install fastapi uvicorn

# copy application
COPY main.py .

# expose service port
EXPOSE 8000

# start server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
