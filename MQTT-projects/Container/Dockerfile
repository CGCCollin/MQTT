FROM python:3
WORKDIR /usr/src/mqttclient

COPY requirements.txt ./
COPY subscribeWithLogging.py ./
#uncomment or update below for CA key and cert.
#COPY CAFILE.cert ./
#COPT CAKEY.key ./
COPY cert.cer ./
COPY key.key ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 10000
CMD ["python","./subscribeWithLogging.py"]

