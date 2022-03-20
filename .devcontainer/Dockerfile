ARG VARIANT='3.10-bullseye'
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# Provides a container with all needed for some MMAI RNN goodness
RUN apt-get update -y \
    && apt-get install -y cmake libgl1-mesa-glx ffmpeg libsm6 libxext6 \
                       libxrender-dev protobuf-compiler \
    && rm -r /var/lib/apt/lists/*
                       
RUN python3 -m pip install --no-cache-dir --upgrade pip
RUN python3 -m pip install --no-cache-dir pandas numpy matplotlib plotly \
     jupyter scikit-learn scipy xgboost opencv-python
RUN python3 -m pip install tqdm  # for progress bars
RUN python3 -m pip install tensorflow
