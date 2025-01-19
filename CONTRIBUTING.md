# CONTRIBUTING

# How to run the dockerfile locally

```
FROM python:3.13
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"
```

# Comando per creare ed avviare dockerfile

```

docker build -t flask-smorest-api .

docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-smorest-api

docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-smorest-api sh -c  "flask run --host 0.0.0.0" se si ha un dockerfile con CMD diverso 
```
# DI BASE L'URL è : http://127.0.0.1:5000 se eseguito localmente
