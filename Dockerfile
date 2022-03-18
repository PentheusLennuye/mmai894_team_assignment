FROM python:3.9-bullseye

# Provides a container with all needed for some MMAI RNN goodness
# Outside a VS Code devcontainer, use as follows:

# Build:
# docker build -t <image name> .  # e.g. docker build -t gmc/mmai .

# Run a python script in the local directory:
# docker run --rm -v $(pwd):/app <image name> <python file>

# Open a jupyter notebook in the local directory:
# docker run --rm -v $(pwd):/app -p 8888:8888 <image name> \
#   jupyter-notebook (notebook)

LABEL author='George Cummings'
USER root
RUN apt-get update -y
RUN apt install libgl1-mesa-glx -y
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install pandas numpy matplotlib plotly jupyter \
                           scikit-learn scipy xgboost
RUN python3 -m pip install opencv-python

RUN useradd -ms /bin/bash apprunner
RUN mkdir /app && chown apprunner /app
USER apprunner
WORKDIR /app
ENTRYPOINT ["python3"]
