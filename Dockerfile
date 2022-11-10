FROM python:3


COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./pago46 .

EXPOSE 8000