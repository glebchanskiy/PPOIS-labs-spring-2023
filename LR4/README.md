# ATM Model- LR4

## Install

Clone repository:

```sh
git clone https://github.com/glebchanskiy/PPOIS-sem4-lab4
```

Install python deps:

```sh
cd lab4
poetry shell
poetry install
```

## Run

Run db:

```sh
cd lab4/postrgres-db
docker-compose up
```

Run game:

```sh
cd lab4
# run cli atm:
poetry run cli

# run gui atm:
poetry run gui
```

## Example usage cli:

```sh
# account transfers and info
poetry run cli -c 1111111111111111 -p 1111 -it
# withdraw 20 usd/byn
poetry run cli -c 1111111111111111 -p 1111 -w 20
# phone payment 33 usd/byn
poetry run cli -c 1111111111111111 -p 1111 -o +333-33-333-33-33=33
```

short flag | long flag| option
--- | --- | ---
-c: | --card | card number
-p: | --pin | card pincode
-i | --info | account info
-t | --transfers | transfers info
-w: | --withdraw | withdraw cash
-o: | --phone | phone payment
-g | --get_card | terminate, get card back

---

## Dependencies

- poetry
- docker
