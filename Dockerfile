FROM python:3.10
WORKDIR /tmp
COPY requirements.txt /tmp

RUN pip install -r requirments.txt

ENTRYPOINT ["python"]
CMD ["main.py"]
