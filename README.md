# Kevin Cowley Challenge

## Instructions to run

`$ docker pull kcowley/sortlists`

`$ docker run kcowley/sortlists [1, 6, 7] [2, 5, 6, 9]`

## Instructions to build image (rather than pulling from docker hub)
- Limit permissions of python file
`$ chmod 755 sort_lists.py`

- Build image (the given image repository:image tag will need to be substituted in the `docker run` command
`$ docker build -t <image>:<tag> .`
