FROM python:3.10-slim
WORKDIR /src
copy . .
expose 4000
RUN pip install -r requirements.txt
CMD python server.py
