FROM python:3.6

# Create app directory
WORKDIR /crawlers

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY . /crawlers

WORKDIR /
EXPOSE 8080
CMD [ "python", "crawlers/main.py" ]
