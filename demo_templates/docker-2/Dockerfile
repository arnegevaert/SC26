FROM ubuntu:latest
RUN apt-get update && apt-get install -y jq curl
CMD ["curl", "--silent", "https://fake-json-api.mock.beeceptor.com/users", "|", "json"]
