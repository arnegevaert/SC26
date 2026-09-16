FROM ubuntu:latest
RUN apt-get update && apt-get install -y jq curl
COPY script.sh /script.sh
CMD ["bash", "/script.sh"]
