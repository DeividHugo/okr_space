FROM python:3.9
EXPOSE 8000

RUN mkdir /app
WORKDIR /app

ADD containers/okr_space_web/requirements.txt .
RUN pip install -r requirements.txt

ADD ../../project .

# Node 
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs

WORKDIR /app/project
RUN npm install

ADD project/static/src ./static/src/
RUN npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css
