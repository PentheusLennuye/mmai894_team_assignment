ARG VARIANT='3.9-bullseye'
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# Provides a container with all needed for some MMAI RNN goodness

RUN apt-get update -y
RUN apt install libgl1-mesa-glx -y
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install pandas numpy matplotlib plotly jupyter \
                           scikit-learn scipy xgboost
RUN python3 -m pip install opencv-python

