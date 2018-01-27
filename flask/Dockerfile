FROM tiangolo/uwsgi-nginx-flask:python3.5

# Copy over and install the requirements
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./mqtt.py /mqtt.py

COPY ./app /app

