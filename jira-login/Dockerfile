FROM python:3.11-alpine

COPY . /app
WORKDIR /app

RUN pip install -r /app/requirements.txt

ENV FLAG = flag{D0_You_LIKE_Th3_Rabanades}
ENTRYPOINT ["python"]
CMD ["app.py"]
