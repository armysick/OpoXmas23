FROM python:3.12


WORKDIR /app/wtv

RUN echo 'flag{Som3_T4sTy_Filhoxxes}'> index.html

RUN useradd -ms /bin/bash flaskit

USER flaskit

COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt
COPY templates/ /app/templates/

WORKDIR /app/

RUN pip install -r requirements.txt

EXPOSE 5000

USER root

COPY runall.sh /root/runall.sh

RUN chmod +x /root/runall.sh

ENTRYPOINT ["/root/runall.sh"]
