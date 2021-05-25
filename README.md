# YO

The *YO*ga videos API

## how to use

- install deps using `pip install -r requirements.txt`
- have the data/ folder at the root of this directory
- create and fill the datbase with `python data_import/import.py`
- start the server with `uvicorn server.main:app`
	- Optionally add the `--reload` parameter to the uvicorn call

## TODO

- [X] list the different attributes
- [X] search episodes by attributes
- [X] full text search
	- [ ] trigram ?
- [X] db fetch tools
- [ ] ~~browsable API~~
- [X] episode.tag -> FK
- [ ] change Episode.series_index to a fk to the related episode when present
	- [ ] dual link ?
- [ ] add creation date to episodes
- [ ] sorting options on episode lists/search
- [ ] add error handling
- [ ] user accounts
- [ ] add a Seen M2M between users and videos
- [ ] add a frontend, maybe