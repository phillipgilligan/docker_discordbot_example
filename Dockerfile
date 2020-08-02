#Our base image
FROM python:alpine3.10
#Setting our working directory
WORKDIR /app 
#Copying contents of all files to our working directory
COPY . /app
#Installing any dependencies
RUN pip install -r requirements.txt
#Exposing port 5000
EXPOSE 5000
#Running our python application
CMD python ./main.py
