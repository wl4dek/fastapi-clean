# FastAPI + Clean Arquiteture


## Clone project
> Clone repo
```
git clone https://github.com/wl4dek/fastapi-clean
```

## Start project
> Create a virtual env
```
python -m venv env
```

> Install dependences
```
pip install -R requirements.txt
```

> Start Server
```
uvicorn src.main:app --reload
```

## If you like run project in docker

```
docker-compose -f "docker-compose.yml" up -d --build
```

## Settings
Create a file **.env** like a **exemple.env**. In the variavel **DB_URL** you put the database url.

In this project I'm using **SQLite**. But we can use another database. Just set this in the **.env** file in the **DB_URL** variable
