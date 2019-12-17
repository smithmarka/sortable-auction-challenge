FROM python:3.8

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src src
CMD ["/src/run.sh"]