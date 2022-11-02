FROM ubuntu:kinetic-20220830  
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y python3 python3-pip python3-dev virtualenv

WORKDIR /data 
COPY . .
RUN ["chmod", "+x", "run.sh"]
CMD sh -c "./run.sh"