FROM python:3.11-alpine

COPY . /app
WORKDIR /app

RUN pip install -r /app/requirements.txt

ENV FLAG_XSS = ZmxhZ3tZb3VfV2lsbF9yZWdyZXRfZVhjZVNTXzBmX0xlaXQ0MH0=
ENTRYPOINT ["python"]
CMD ["app.py"]
