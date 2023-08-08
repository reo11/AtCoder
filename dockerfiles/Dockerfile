FROM ubuntu:18.04

ARG UID
ARG UNAME
RUN useradd $UNAME -u $UID -m

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    software-properties-common build-essential \
    curl wget apt-utils libboost-all-dev libssl-dev git peco golang \
    dconf-tools \
    apt-transport-https ppa-purge \
    ca-certificates\
    tar zip unzip zlib1g-dev bzip2 libbz2-dev \
    openssl libssl-dev \
    zsh vim screen tree htop \
    net-tools lynx iftop traceroute \
    sudo

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

RUN rm -f /usr/bin/python && ln -s /usr/bin/python3 /usr/bin/python

# Rust
ENV RUST_VERSION 1.66.1
ENV RUST_HOME /home/${UNAME}/.cargo
ENV RUSTUP_HOME ${RUST_HOME}/rustup
ENV CARGO_HOME ${RUST_HOME}/cargo
ENV PATH $PATH:$HOME/.cargo/bin
ENV PATH $PATH:$CARGO_HOME/bin

RUN mkdir $RUST_HOME && \
    chown -R $UNAME $RUST_HOME

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs > ${RUST_HOME}/rustup.sh && \
    chmod +x ${RUST_HOME}/rustup.sh && \
    ${RUST_HOME}/rustup.sh -y --default-toolchain $RUST_VERSION --no-modify-path

RUN rustup update
RUN rustup install $RUST_VERSION
RUN rustup install 1.42.0
RUN rustup component add clippy rls rust-analysis rust-src rust-docs rustfmt

# RUN cargo +stable install racer
RUN cargo +1.66.1 install cargo-compete
# RUN cargo install clippy
# RUN cargo install cargo-cache
# RUN cargo +nightly install racer
# RUN cargo install cargo-src
# RUN cargo install cargo-watch
# RUN cargo install cargo-tree
# RUN cargo install cargo-asm
# RUN cargo install cargo-expand
# RUN cargo install --git https://github.com/japaric/cargo-binutils
# RUN cargo install cargo-check
# # rootけんげんが必要とか言われるので消す
# RUN cargo cache -a

RUN chown -R $UNAME $RUST_HOME

# online-judge-tools
RUN python3.8 -m pip install online-judge-tools

# その他のコマンド
RUN mkdir /work
# RUN go get github.com/motemen/ghq

# zsh
RUN apt install -y sudo
RUN mkdir /tmp/tmphome &&\
    cd /tmp/tmphome &&\
    git clone https://github.com/reo11/dotfiles.git &&\
    ./dotfiles/.bin/dotsinstaller.sh --no-gui &&\
    vim -c PlugInstall -c q -c q
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/zdharma/zinit/master/doc/install.sh)"

# ユーザ名の指定
# ARG UID
# ARG UNAME
# RUN useradd $UNAME -u $UID -m
# USER $UNAME

USER $UNAME

ENV PATH $PATH:$HOME/.cargo/bin
ENV PYTHONPATH=$PYTHONPATH:/work
# ENV RUSTUP_TOOLCHAIN 1.42.0

# fix symbolic link for rust 1.42.0
# https://zenn.dev/yajamon/articles/be689814d242f8
# RUN cd /home/reo/.cargo/rustup/toolchains/1.42.0-x86_64-unknown-linux-gnu/lib/rustlib/src/rust && \
#     ln -sv src library

COPY ./config/.zshrc /tmp/.zshrc
RUN cat "/tmp/.zshrc" >> ~/.bashrc
WORKDIR /work
