FROM python:slim
ENV TOKEN=''
COPY . .
RUN pip install -r requirements.txt
CMD python bot.py