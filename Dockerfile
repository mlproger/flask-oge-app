FROM python:3.10

WORKDIR /app
RUN pip install -r requirments.txt

ENTRYPOINT ["python"]
CMD ["main.py"]
