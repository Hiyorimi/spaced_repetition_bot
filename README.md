# Spaced repetition bot

This is a bot which sends you back anything several times to make you remember things better.


## Setup

### Local setup

```bash
cp env.template ./.env
poetry install
poetry run python3 main.py
```

### Docker setup

```bash
git clone git@github.com:Hiyorimi/spaced_repetition_bot.git
docker build -t spaced_repetition_bot 
docker run -d --name spaced_repetition_bot -e ENV=production -e API_TOKEN=1111:YOUR_TOKEN spaced_repetition_bot python3 main.py.
```
