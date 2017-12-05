# CDmon test

This repo contains the code for the CDmon test. It's been split in two different directories, each one contains the code and stuff needed.

## Exercise 1

So you'd need a personal Digital Ocean key. Remember that you need to install docker in your machine (your mileage may vary, for Linux check your package manager, for Windows and MacOs, go to the official site and download them). After that, open a command line and run the following commands (I’m assuming a UNIX machine, for Windows probably you’d need to use back slashes instead):

```
# docker-machine create --driver digitalocean \ --digitalocean-access-token ${DIGITAL_OCEAN_TOKEN} ${DROPLET_NAME} [1]
# eval $(docker-machine env ${DROPLET_NAME})
# cd ${GUS_GITHUB_REPO}/ex1
# docker-compose build --up -d
```
Please replace **${DIGITAL_OCEAN_TOKEN}** with your personal token generated in Digital Ocean and **${DROPLET_NAME}** with the name of your droplet. **${GUS_GITHUB_REPO}** is the directory where you cloned the repo.

This will connect to your droplet, build the latest image of the official docker container from Apache (which uses the latest version of 2.4, tagged as latest) and run it in the droplet.

## Exercise 2

To test this one, the only thing needed is run the Jenkins docker container. Assuming that you ran [1], you only need to run:

```
# cd ${GUS_GITHUB_REPO}/ex2/jenkins && docker-compose build --up -d
```
Point your browser to your droplet IP (port 8080) and there you should have your Jenkins:

```
http://${DROPLET_IP}:8080
```
If you want to test mine, use the IP provided by mail. The user is **cdmon** and the credentials are also provided by mail.     

[1] eval $(docker-machine env ${DROPLET_NAME)}

afegit per CDmon
