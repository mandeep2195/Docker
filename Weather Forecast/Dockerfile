FROM python:3.11.5
WORKDIR /myapp
COPY weatherForcastAPI.py /myapp/weatherForcastAPI.py
RUN pip install requests
CMD [ "python", "./weatherForcastAPI.py" ]