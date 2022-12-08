FROM python:3.10
WORKDIR /tmp
COPY requirements.txt /tmp/requirements.txt
COPY main.py /tmp/main.py
COPY config.py /tmp/config.py

RUN pip install -r /tmp/requirements.txt

ENTRYPOINT ["python"]
CMD ["main.py"]
