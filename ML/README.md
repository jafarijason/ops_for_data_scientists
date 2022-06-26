

## Installing pip for Python 3
```
sudo apt update
sudo apt install python3-pip
```

## Installing virtualenv
```
python3 -m pip install --user virtualenv
sudo pip3 install virtualenv
```

```
cd ML
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt

```

```
python train_and_save_a_model 
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