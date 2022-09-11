# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONUNBUFFERED=1

# install ssh
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y openssh-server

# install vim
RUN apt-get install -y vim

# opencv 를 이용하기 위한 설치
RUN apt-get update
RUN apt-get -y install libgl1-mesa-glx


# 작업 폴더 설정
WORKDIR /home
RUN mkdir "model"
WORKDIR /home/backend

# 파이썬 라이브러리 설치
COPY requirements.txt /home/backend
RUN pip install -r requirements.txt

# 개발용으로 entrypoint.sh 파일를 연결
ENTRYPOINT ["sh", "/home/backend/entrypoint.sh"]