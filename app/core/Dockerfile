FROM python:3.9
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN  pip install -r requirements.txt  
EXPOSE 5000
RUN chmod +x /app/init_app.sh
RUN chmod +x /app/init_app_dev.sh


ENTRYPOINT ["/app/init_app.sh"]
