#!/bin/bash

set -e

# buildimage rebuilds the docker image used by the CI server.
buildimage() {
  cd builder-docker
  docker build -t alkasir-centraladmin-builder .
}


# runci is used inside the docker container above when running a build.
runci() {
  set -x
  pip install --cache-dir=../pip-cache flake8
  flake8 --config=tox.ini
  pip install --cache-dir=../pip-cache -r requirementsgf.txt
  python manage.py test
  python manage.py migrate
}


case ${1} in
  runci|buildimage)
    ${1}
    ;;
  *)
    echo "Usage: ${0} runci"
    echo "Usage: ${0} buildimage"
    ;;
esac
