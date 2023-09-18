FROM python:3.10.5

RUN apt-get update && apt-get install -y \
  python3-pip

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]