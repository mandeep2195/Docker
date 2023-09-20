FROM python:3.7
WORKDIR /myapp
COPY checks.py /myapp/checks.py
RUN pip install psutil
CMD [ "python", "./checks.py" ]