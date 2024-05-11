FROM jenkins/jenkins:latest

USER root

# Install Python3 and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

USER jenkins
