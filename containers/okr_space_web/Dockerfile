FROM python:3.9
EXPOSE 8000

RUN mkdir /app
WORKDIR /app

ADD containers/okr_space_web/requirements.txt .
RUN pip install -r requirements.txt

ADD ../../project .
