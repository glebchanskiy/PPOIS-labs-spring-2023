# Kivy Application - LR2

## Install

Clone repository:

```sh
git clone https://github.com/glebchanskiy/PPOIS-sem4-lab2
```

Install python deps:

```sh
cd lab2
poetry install
```

## Run

Start db:

```sh
cd lab2/postgres-db
docker-compose up
```

Run app:

```sh
cd lab2
poetry run app
```

## Build

To create an executable file you can use any builder. 
For `macos` simple run:

```sh
cd lab2
./createDMG
```

---

## Dependencies

- poetry
- docker
