FROM python:3.10

WORKDIR /app
COPY requirements.txt/ app/
RUN pip install -r requirments.txt

ENTRYPOINT["python"]
CMD["main.py"]
