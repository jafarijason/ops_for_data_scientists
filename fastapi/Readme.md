# install virtualenv on ubuntu [here](https://gist.github.com/frfahim/73c0fad6350332cef7a653bcd762f08d)

```
virtualenv venv

source venv/bin/activate

```

# Install FastAPI

```
pip install "fastapi[all]"
```

```
pip freeze  >  requirements.txt
```

```
uvicorn main:app --reload --host 0.0.0.0
```

```
127.0.0.1:8000/docs
```