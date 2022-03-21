# [Save and Load Machine Learning Models in Python with scikit-learn](https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/)

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
cd Save_And_Load_ML
virtualenv env
source ./venv/bin/activate
pip install pandas sklearn

pip freeze  >  requirements.txt

```

```
python save_model.py
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