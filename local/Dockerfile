FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive \
    CONDA_DIR=/opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH

# We need the ssh client
RUN apt-get update && apt-get -y install --no-install-recommends openssh-client

# setup conda for our Python environment
RUN apt-get -y install wget \
 && wget -O miniforge.sh https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-$(uname -m).sh \
 && bash miniforge.sh -b -p $CONDA_DIR \
 && rm miniforge.sh

# install ipyparallel with mpi/openmpi
RUN mamba install -y ipyparallel jupyterlab

# make the user we are going to use
# with username `demo` and password `whocares`
ENV USER=demo \
    SHELL=/bin/bash
RUN useradd -m -s $SHELL ${USER}

# create the 'local' remotempi profile
ENV HOME=/home/${USER}
WORKDIR $HOME
USER demo
RUN ipython profile create --parallel remotempi
COPY --chown=${USER}:0 ipcluster_config.py $HOME/.ipython/profile_remotempi/ipcluster_config.py

# set the jupyter server password
# so we don't need to deal with tokens
ENV JUPYTER_PLATFORM_DIRS=1
COPY --chown=${USER}:0 jupyter_server_config.py $HOME/.config/jupyter/jupyter_server_config.py

# run jupyterlab
EXPOSE 8888
WORKDIR /home/demo
CMD ["jupyter-lab", "--ip=''", "--port=9999", "--no-browser"]
