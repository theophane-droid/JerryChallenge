# Jerry Challenge

      ()()         ____
      (..)        /|o  |
      /\/\       /o|  o|
     c\db/o...  /o_|_o_|

Welcome in the Jerry Challenge !

Your goal is to help jerry to get the cheese in only five seconds.

## How to install

On linux :

```bash
git clone https://github.com/theophane-droid/JerryChallenge
cd JerryChallenge
```

Then, you can create your flags :
```bash 
echo mysecretflag1 > flag02.txt
echo mysecretflag1 > flag03.txt
echo mysecretflag1 > flag04.txt
```
Where are flag01 & flag02 ? Look closely at this repository ;)

Let's go !

```bash
python3 src/games.py
```

## Network setup

To enable remote access to Jerry Challenge you can do the following :

```bash
netcat -klnvp 4444 -e "$(pwd)/src/game.py"
```

## Network setup with docker

You can also setup Jerry Challenge with docker :

```bash
docker build . -t jerrychallenge
docker run -d --restart always -p output_port:5000 --name jerrychallenge jerrychallenge:latest
```


## How to play

Your are Jerry (£) and you have to get the cheese (^) in 5 seconds.

You can move Jerry with the instructions left, right, up, or down.

Maybe your little fingers won't be fast enough...