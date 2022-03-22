FROM python:latest

WORKDIR /code

COPY . /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


RUN python save_model.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
