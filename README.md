# Bitly-creator
The script make urls shorter and shows how many times followed the url. 

# How to start

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

### Environment variables.

- token

.env example:

```
token=token=c011g67b5df7470360ab5a34ft462d107da143a9
```
### How to get

1. Sign up [bit.ly](https://bit.ly)

2. Bitly offers several types of tokens. You need GENERIC ACCESS TOKEN. Use e-mail instead of social networks. It will simplify receiving a token.

### Run

Launch on Linux(Python 3.5) or Windows as simple

```bash
$ python main.py https://mysite.com

# You will see

$ python main.py https://mysite.com
Short url: http://bit.ly/2wpKUfq
Your url was clicked 5 time(s) 
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)