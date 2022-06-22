FROM selenium/standalone-chrome

USER root
RUN wget https://bootstrap.pypa.io/get-pip.py

RUN apt-get update -y && apt-get install -y python3-distutils

RUN python3 get-pip.py
RUN python3 -m pip install selenium

WORKDIR /app

ADD scraper.py .

ENTRYPOINT ["python3", "/app/scraper.py"]
