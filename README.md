# ShorterFYI

'Shorter for your information' is a [URL shortener](http://en.wikipedia.org/wiki/URL_shortening).

## Install

Clone the repository:
```bash
$ git clone git@github.com:shektor/shorter-fyi.git
$ cd shorter-fyi
```

Create a virtualenv and activate it:
```bash
$ python3 -m venv env
$ . env/bin/activate
```

Install package requirements:
```bash
$ pip install -r requirements.txt
```

Configure environment variables:
```bash
$ touch .env

# Add following lines to .env file and save
FLASK_APP=shorter-fyi
FLASK_ENV=development
```

## Run

```bash
$ flask run
```
Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in a browser.

## Test

```bash
> pytest
```



