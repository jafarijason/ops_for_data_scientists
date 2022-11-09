# [Save and Load Machine Learning Models in Python with scikit-learn](https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/)

## Make sure you have python3 installed in your machine


## Installing virtualenv
```
python3 -m pip install --user virtualenv

```

```
python3 -m venv venv
```

```
source ./venv/bin/activate
pip3 install -r requirements.txt
```

### For save model
```
python3 save_model.py
```

### For load model and prediction
```
python3 loadAndPredict.py
```

# [FastAPI](https://fastapi.tiangolo.com/)

## Installing FastAPI
```
pip3 install "fastapi[all]"
# or
pip3 install fastapi
pip3 install "uvicorn[standard]"

pip3 freeze  >  requirements.txt

```


```
uvicorn main:app --reload
uvicorn main:app --host 0.0.0.0  --reload
```

# Docker


```
docker build -t overview:1.0.1 .
docker run -d --name myContainerOverView -p 8000:8000 overview:1.0.1
```

```
docker-compose build
docker-compose up
docker-compose down
docker-compose up -d
```

# [Docker Swarm Rocks](https://dockerswarm.rocks/)

```
export DOMAIN=ml.jasonjafari.com
export NODE_ID=$(docker info -f '{{.Swarm.NodeID}}')
docker stack deploy -c saveMl.yml  ml --resolve-image=always --with-registry-auth --prune
```
