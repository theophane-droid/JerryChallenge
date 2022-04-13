from debian:10

user root
run apt -y update
run apt -y install netcat python3

copy ./ /app
copy ./src /app/src
workdir /app
run chmod +x /app/src/game.py

# cmd ls /app/src
cmd nc -lnvp 5000 -e /app/src/game.py