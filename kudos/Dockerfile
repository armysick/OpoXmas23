FROM python:3.11-alpine

COPY . /app
WORKDIR /app

RUN pip install -r /app/requirements.txt

ENV FLAG_KUDOS=flag{KudFish_M3ans_Bacalhau}
ENTRYPOINT ["python"]
CMD ["app.py"]
