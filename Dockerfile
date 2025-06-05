FROM python:3.13

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 5000

CMD ["python", "current_time.py"]