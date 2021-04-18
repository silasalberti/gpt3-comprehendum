FROM python:latest

RUN pip install --upgrade pip

COPY . /usr/src/app

RUN CFLAGS="-Wno-narrowing" pip install cld2-cffi
RUN pip install -r /usr/src/app/requirements.txt
RUN pip install slackers
EXPOSE 5000
WORKDIR /usr/src/app
CMD ["uvicorn", "index:app", "--host", "0.0.0.0" ,"--port", "5000", "--log-level", "info"]



