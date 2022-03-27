#!/usr/bin/env bash
docker run --rm -v$(pwd):/app \
	-p 8888:8888 gmc/mmai \
	jupyter-notebook --ip 0.0.0.0 --no-browser
