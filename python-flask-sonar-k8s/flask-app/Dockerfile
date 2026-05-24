FROM python:3.10-slim

WORKDIR /src

COPY src/main/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /src/main .

CMD['python3', 'app.py']