FROM python:3

WORKDIR C:\\Users\Filip Ceglik\Slackbot

ADD requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./dummy.py" ]

EXPOSE 80