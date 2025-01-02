FROM python:3.12

WORKDIR /usr/stc/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

CMD [ "uvicorn", "app.main", "--host", "0.0.0.0", "--port", "8000"]