FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive \
    CONDA_DIR=/opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH

# This image will run as an ssh server
RUN apt-get update && apt-get -y install --no-install-recommends openssh-server

# setup conda for our Python environment
RUN apt-get -y install wget \
 && wget -O miniforge.sh https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-$(uname -m).sh \
 && bash miniforge.sh -b -p $CONDA_DIR \
 && rm miniforge.sh

# install ipyparallel with mpi/openmpi
RUN mamba install -y ipyparallel mpi4py openmpi

# make the user we are going to use
# with username `demo` and password `whocares`
RUN useradd -m -s /bin/bash demo -p "$(openssl passwd -1 whocares)"

# run the ssh server as root
USER root
EXPOSE 22
CMD ["service", "ssh", "start", "-D"]
