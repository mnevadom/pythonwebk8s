FROM alpine:3.1


RUN apk add --update python py-pip

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD webapp.py /src/webapp.py

EXPOSE 8080

CMD ["python", "/src/webapp.py", "-p 8080"]