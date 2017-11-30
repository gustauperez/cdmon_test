# CDmon test

This repo contains the code for the CDmon test. It's been splitted in two different directories, each one contains the code and stuff needed.

## Exercice 1

So you'd need a personal Digial Ocean key. Remember that you need to install docker in your machine (your milleage may vary, for Linux check your package manager, for Windows and MacOs, go to the official site and download them). After that, open a command line and run the following commands (I’m assuming a UNIX machine, for Windows probably you’d need to use back slashes instead):

```
# docker-machine create --driver digitalocean \ --digitalocean-access-token ${DIGITAL_OCEAN_TOKEN} ${DROPLET_NAME} [1]
# eval $(docker-machine env droplet)
# cd ${GUS_GITHUB_REPO}/ex1
# docker-compose build --up -d
```

Please replace ${DIGITAL_OCEAN_TOKEN} with your personal token generated in Digital Ocean and ${DROPLET_NAME} with the name of your droplet.

This will connect to your droplet, build the latest image of the official docker container from Apache (which uses the latest version of 2.4, tagged as latest) and run it in the droplet.

## Exercise 2
