FROM python:3.10

COPY requirements.txt /tmp
WORKDIR /tmp

RUN pip install -r requirments.txt

ENTRYPOINT ["python"]
CMD ["main.py"]
