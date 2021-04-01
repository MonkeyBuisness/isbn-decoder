FROM python:3

WORKDIR /app

COPY ./app /app

RUN apt-get update && \
    apt-get install -y zbar-tools python3-opencv
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3", "main.py", "--f", "(image-file-path)"]
