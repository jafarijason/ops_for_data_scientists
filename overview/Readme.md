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
 

```
python3 save_model.py
```

```
pip install "fastapi[all]"
# or
pip install fastapi
pip install "uvicorn[standard]"

pip freeze  >  requirements.txt

```

```
uvicorn main:app --reload
uvicorn main:app --host 0.0.0.0  --reload
```


```
docker build -t myimage .
docker run -d --name mycontainer -p 8000:8000 myimage
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
