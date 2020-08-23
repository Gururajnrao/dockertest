FROM python:3
LABEL maintainer="Gururaj(gururajnrao@gmail.com)"

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
ENV AZURE_SUBSCRIPTION_ID=722985c7-a1b4-4761-957f-39cd8869a2de
ENV AZURE_CLIENT_ID=759a9130-4788-413b-9383-d0f936e15bf8
ENV AZURE_CLIENT_SECRET=/8L-dzcABc?4]HY3WhIQBEmHncitc6d8
ENV AZURE_TENANT_ID=6f4fe054-7b7c-481e-9614-d66510fecc1b

COPY class_list_tags.py /app
RUN chmod a+x class_list_tags.py

CMD ["./class_list_tags.py"]
