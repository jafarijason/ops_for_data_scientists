# Outline

<ul>
    <li>How to save ML model in a file</li>
    <li>How to load and use saved model</li>
    <li>How FastAPI can help us for serving our ml model</li>
    <li>How Docker can help us to containerize out app</li>
    <li>How docker-compose can save our time for working with docker</li>
    <li>How we can deploy our docker image on cloud (AWS EC2 VM)</li>
    <li>How connect our Visual studio code te the remote linux server server</li>
</ul>

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

# [FastAPI](https://github.com/jafarijason/ops_for_data_scientists/tree/master/fastapi)


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


# [Docker](https://github.com/jafarijason/ops_for_data_scientists/tree/master/docker)


## [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

## [How To Install and Use Docker Compose on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04)

## [How to create Docker Images with a Dockerfile on Ubuntu 20.04 LTS](https://www.howtoforge.com/tutorial/how-to-create-docker-images-with-dockerfile/)

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

```
docker login
```

```
docker-compose push
```

# [Container Orchestration](https://medium.com/@thamilini/container-orchestration-d22c3bd3de7b)

# [Container Orchestration](https://medium.com/onfido-tech/container-orchestration-with-kubernetes-an-overview-da1d39ff2f91)

# [Container Orchestration and Management Options](https://k21academy.com/docker-kubernetes/container-orchestration-and-management-options/)


# [Docker Swarm Rocks](https://dockerswarm.rocks/)

```
export DOMAIN=ml.jasonjafari.com
export NODE_ID=$(docker info -f '{{.Swarm.NodeID}}')
docker stack deploy -c serveModel.yml  ml --resolve-image=always --with-registry-auth --prune
```
