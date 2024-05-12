FROM jenkins/jenkins:latest

USER root

# Install Python3, pip, and curl
RUN apt-get update && \
    apt-get install -y python3 python3-pip curl && \
    rm -rf /var/lib/apt/lists/*

USER jenkins