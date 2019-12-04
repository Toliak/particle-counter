#! /bin/sh

set -ex


docker run -it --rm \
	   -v $(pwd):/opt/builder/ \
	   -w /opt/builder/demo \
           toliak/course-project-2019:$@
