FROM python:3

WORKDIR C:\\Users\Filip Ceglik\Slackbot

ADD requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD [ "python", "./dummy.py" ]