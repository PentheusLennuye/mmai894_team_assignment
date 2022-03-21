#!/bin/bash
# To be used if Docker and VS Code is not used
uname -m | grep amd64 && python3 -m pip install tensorflow; true
uname -m | grep aarch64 && python3 -m pip install tensorflow-aarch64 \
        -f https://tf.kmtea.eu/whl/stable.html; true
