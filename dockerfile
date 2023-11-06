FROM python:alpine3.10
RUN pip install --upgrade pip

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt

COPY . /app
EXPOSE 5000
EXPOSE 27017
CMD python app/index.py