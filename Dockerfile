FROM python:3.8-slim

# set work directory
WORKDIR /app

# install dependencies
# RUN pip install --upgrade pip
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy files/folders
COPY . .

EXPOSE 5000

CMD [ "flask", "run","--host","0.0.0.0","--port","5001"]

