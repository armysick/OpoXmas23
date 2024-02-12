FROM python:3.11-alpine

COPY . /app
WORKDIR /app

RUN pip install -r /app/requirements.txt

ENV FLAG_GUID=flag{I_L0v3_ALettery}
ENTRYPOINT ["python"]
CMD ["app.py"]
