FROM python:slim
WORKDIR /app
EXPOSE 8000
COPY . /app 
CMD ["python3","app.py"]
