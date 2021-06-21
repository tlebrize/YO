# YO

The *YO*ga videos API

## how to use

- install deps using `pip install -r requirements.txt`
- have the data/ folder at the root of this directory
- start redisand postgres with `docker-compose up -d`
- start the server with `uvicorn server.main:app`
	- Optionally add the `--reload` parameter to the uvicorn call for backend hotreload.
- migrate the database schemas with `aerich upgrade`
- fill the datbase with `curl http://localhost:8000/load_data/`
