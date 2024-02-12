FROM python:3.6-slim-buster

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV FLAG={Prototype_Of_A_K!ng_Cak3}

ENTRYPOINT ["python"]
CMD ["app.py"]
