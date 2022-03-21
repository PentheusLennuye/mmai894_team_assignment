FROM python:3.10-bullseye
ARG TARGETPLATFORM

# Provides a container with all needed for some MMAI RNN goodness
# This requires Docker with the BuildKit backend.

# Build:
# DOCKER_BUILDKIT=1 docker build -t <image name> .  # e.g. docker build -t gmc/mmai .

# Run a python script in the local directory:
# docker run --rm -v $(pwd):/app <image name> <python file>

# Open a jupyter notebook in the local directory:
# docker run --rm -v $(pwd):/app -p 8888:8888 <image name> \
#   jupyter-notebook (notebook)

LABEL author='George Cummings'
USER root
RUN apt-get update -y \
    && apt-get install -y cmake libgl1-mesa-glx ffmpeg libsm6 libxext6 \
                       libxrender-dev protobuf-compiler \
    && rm -r /var/lib/apt/lists/*
                       
RUN python3 -m pip install --no-cache-dir --upgrade pip
RUN python3 -m pip install --no-cache-dir pandas numpy matplotlib plotly \
     jupyter scikit-learn scipy xgboost opencv-python
RUN python3 -m pip install tqdm  # for progress bars

RUN if [ "$TARGETPLATFORM" = "linux/amd64" ]; then \
	python3 -m pip install tensorflow; fi

RUN if [ "$TARGETPLATFORM" = "linux/arm64" ]; then \
	python3 -m pip install tensorflow-aarch64 \
        -f https://tf.kmtea.eu/whl/stable.html; fi

RUN useradd -ms /bin/bash apprunner
RUN mkdir /app && chown apprunner /app
USER apprunner
WORKDIR /app
CMD ["python3"]
