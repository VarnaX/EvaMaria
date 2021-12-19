#
FROM python:3.8-slim-buster
RUN apt update && apt upgrade -y
RUN apt install git -y

RUN mkdir /EvaMaria
WORKDIR /EvaMaria
RUN chmod 777 /EvaMaria


COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash", "start.sh"]