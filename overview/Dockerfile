FROM python:3.9

RUN pip install --upgrade pip

WORKDIR /code

COPY save_model.py /code
COPY main.py /code
COPY requirements.txt /code

RUN pip install --no-cache-dir -r /code/requirements.txt

RUN python save_model.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
EXPOSE 8000