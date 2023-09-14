# Briareus
Testing my skills by creating an end-to-end DevOps project, covering containerisation, orchestration, infrastructure as code, cloud computing, and much more. The repo is named after Briareus, a Greek god (a DevOps Engineer) with 100 arms (tools at our disposal)!

# The Python app - a simple CLI-based Pokemon battle simulator

This game was inspired by Episode 24 of Pokemon, appropriately named 'Haunter vs Kadabra'!

As Ash Ketchum alongside Haunter, you face off against Gym Leader Sabrina and her Kadabra in a Pokemon battle. By choosing Haunter's moves and using the available items, your aim is to win!

![](https://static.wikia.nocookie.net/pokemon/images/6/60/TB024_13.jpg/revision/latest?cb=20131105221914)

Please note that this is a fan-made simulator, and all rights to the official Pokemon assets depicted in this game are property of the Pokemon Company.

## Dockerfile instructions

docker build -t briareus_v1 .
docker run -it briareus_v1