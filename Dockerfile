#Our base image
FROM ubuntu:latest
#Setting our working directory
WORKDIR /app 
#Copying contents of all files to our working directory
COPY . /app
#Updating package manager
RUN apt update -y
#Required dependency apt-utils
RUN apt install apt-utils
#Required dependency software-properties-common
RUN apt install software-properties-common -y
#Adds required repo for Python3
RUN add-apt-repository ppa:deadsnakes/ppa -y
#Final Update just in case to apt package manager
RUN apt update -y
#Installs Python 3
RUN apt install python3.8 -y
#Installs pip package manager for dependencies
RUN apt install python3-pip -y
#Installs dependencies for discord bot
RUN pip3 install -r requirements.txt
#Exposing port 5000
EXPOSE 5000
#Running our python application
CMD python3 ./main.py
