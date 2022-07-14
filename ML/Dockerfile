FROM python:latest

WORKDIR /code

COPY trainAndSaveModel.py /code
COPY main.py /code
COPY requirements.txt /code

RUN pip install --no-cache-dir -r /code/requirements.txt

RUN ls -la

RUN python trainAndSaveModel.py

RUN ls -la

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
