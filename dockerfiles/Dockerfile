FROM ubuntu:18.04
RUN apt-get update &&\
    apt-get install -yq software-properties-common wget zlib1g lbzip2 apt-utils libboost-all-dev git peco golang

RUN export GOPATH=$HOME/go &&\
    export PATH="$GOPATH/bin:$PATH"

# Python 3.8.2
RUN add-apt-repository -y ppa:deadsnakes/ppa &&\
    apt install -y python3.8 python3.8-dev python3-pip &&\
    python3.8 -m pip install --upgrade pip setuptools &&\
    python3.8 -m pip install -U Cython numba numpy scipy scikit-learn networkx

# C++
RUN apt-get install -y software-properties-common &&\
    add-apt-repository -y ppa:ubuntu-toolchain-r/test &&\
    apt install -y gcc-9 g++-9 gdc-9 gfortran-9

RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 10 &&\
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 10 &&\
    update-alternatives --install /usr/bin/gdc gdc /usr/bin/gdc-9 10 &&\
    update-alternatives --install /usr/bin/gfortran gfortran /usr/bin/gfortran-9 10

RUN git clone https://github.com/boostorg/boost.git &&\
    cd boost &&\
    git submodule update --init &&\
    chmod 777 bootstrap.sh &&\
    ./bootstrap.sh --with-toolset=gcc --without-libraries=mpi,graph_parallel --with-python=python3.8 &&\
    ./b2 -j3 toolset=gcc variant=release link=static runtime-link=static cxxflags="-std=c++17" stage &&\
    ./b2 -j3 toolset=gcc variant=release link=static runtime-link=static cxxflags="-std=c++17" --prefix=/opt/boost/gcc install

# PyPy3 (7.3.0)
RUN add-apt-repository -y ppa:pypy/ppa &&\
    apt update &&\
    apt install -y pypy pypy3

# Rust
RUN apt -y install rust-all

# online-judge-tools
RUN python3.8 -m pip install online-judge-tools

# その他のコマンド
RUN mkdir /work
# RUN go get github.com/motemen/ghq

# zsh
# RUN apt install -y sudo
# RUN mkdir /tmp/tmphome &&\
#     cd /tmp/tmphome &&\
#     git clone https://github.com/reo11/dotfiles.git &&\
#     ./dotfiles/.bin/dotsinstaller.sh --no-gui &&\
#     vim -c PlugInstall -c q -c q
# RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/zdharma/zinit/master/doc/install.sh)"

# ユーザ名の指定
# ARG UID
# ARG UNAME
# RUN useradd $UNAME -u $UID -m
# USER $UNAME
ARG UID
ARG UNAME
RUN useradd $UNAME -u $UID -m
USER $UNAME

ENV PYTHONPATH=$PYTHONPATH:/work

COPY ./config/.zshrc /tmp/.zshrc
RUN cat "/tmp/.zshrc" >> ~/.bashrc
WORKDIR /work
