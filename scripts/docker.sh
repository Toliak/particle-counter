#! /bin/sh

set -ex

docker build . --tag particle_counter
docker stop particle_counter_cont || true

# sleep 2

docker run -it --rm \
	   -v $(pwd):/opt/builder/ \
	   --name particle_counter_cont \
           particle_counter $@
