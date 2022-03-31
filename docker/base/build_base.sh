#!/bin/bash
#./build_base.sh 1.0.0
set -euo pipefail

tag="giftless-base-$1"

full_tag="registry.pyn.ru/giftless-base:$tag"
DOCKER_BUILDKIT=1 docker build --ssh default --progress plain --no-cache --tag "$full_tag" .
docker push "$full_tag"
