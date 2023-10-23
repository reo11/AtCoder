FROM --platform=linux/x86_64 pypy:3.10-7.3.12-slim-bookworm

# AtCoder Language Update
# https://docs.google.com/spreadsheets/d/1HXyOXt5bKwhKWXruzUvfMFHQtBxfZQ0047W7VVObnXI/edit#gid=521804310

# ユーザの追加
ARG UID
ENV USER_NAME=player
RUN useradd $USER_NAME -u $UID -m

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update &&\
    apt-get install -y --no-install-recommends \
    sudo

# Python
RUN cd /tmp &&\
    sudo apt update &&\
    # 依存関係のインストール。 参考:https://devguide.python.org/getting-started/setup-building/#build-dependencies
    sudo env DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true apt install -y build-essential --fix-missing gdb lcov pkg-config \
        libbz2-dev libffi-dev libgdbm-dev libgdbm-compat-dev liblzma-dev \
        libncurses5-dev libreadline6-dev libsqlite3-dev libssl-dev \
        lzma lzma-dev tk-dev uuid-dev zlib1g-dev git \
        libgmp-dev libmpfr-dev libmpc-dev wget tar

RUN wget https://www.python.org/ftp/python/3.11.4/Python-3.11.4.tar.xz -O Python-3.11.4.tar.xz &&\
    tar xf Python-3.11.4.tar.xz &&\
    cd Python-3.11.4 &&\
    ./configure --enable-optimizations &&\
    make &&\
    sudo make altinstall &&\
    cd ..

RUN python3.11 -m pip install \
        numpy==1.24.1 \
        scipy==1.10.1 \
        networkx==3.0 \
        sympy==1.11.1 \
        sortedcontainers==2.4.0  \
        more-itertools==9.0.0 \
        shapely==2.0.0 \
        bitarray==2.6.2 \
        PuLP==2.7.0 \
        mpmath==1.2.1 \
        pandas==1.5.2 \
        z3-solver==4.12.1.0 \
        scikit-learn==1.2.0 \
        ortools==9.5.2237 \
        polars==0.15.15 \
        gmpy2==2.1.5 \
        numba==0.57.0 \
        git+https://github.com/not522/ac-library-python &&\
    python3.11 -m pip install -U setuptools==66.0.0 &&\
    python3.11 -m pip install cppyy==2.4.1

# pypy3
RUN cd /tmp

RUN apt-get update &&\
    apt-get install -y --no-install-recommends \
    wget tar

# pipを使えるようにする
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN pypy3 get-pip.py --break-system-packages
# numpyなど各種ライブラリを入れるのに必要
RUN sudo apt install -y gcc g++ gfortran libopenblas-dev liblapack-dev pkg-config libgeos-dev

RUN pypy3 -mpip install --break-system-packages numpy==1.24.1
# RUN pypy3 -mpip install --break-system-packages scipy==1.10.1
RUN pypy3 -mpip install --break-system-packages networkx==3.0
RUN pypy3 -mpip install --break-system-packages sympy==1.11.1
RUN pypy3 -mpip install --break-system-packages sortedcontainers==2.4.0
RUN pypy3 -mpip install --break-system-packages more-itertools==9.0.0
RUN pypy3 -mpip install --break-system-packages shapely==2.0.0
RUN pypy3 -mpip install --break-system-packages bitarray==2.6.2
RUN pypy3 -mpip install --break-system-packages PuLP==2.7.0
RUN pypy3 -mpip install --break-system-packages mpmath==1.2.1
RUN pypy3 -mpip install --break-system-packages pandas==1.5.2
RUN pypy3 -mpip install --break-system-packages z3-solver==4.12.1.0
# RUN pypy3 -mpip install --break-system-packages scikit-learn==1.2.0
RUN pypy3 -mpip install --break-system-packages typing-extensions==4.4.0
RUN pypy3 -mpip install --break-system-packages cppyy==2.4.1
RUN pypy3 -mpip install --break-system-packages git+https://github.com/not522/ac-library-python

# online-judge-tools
RUN python3.11 -m pip install online-judge-tools

# その他のコマンド
RUN mkdir /work

# ユーザ切り替え
USER $USER_NAME

ENV PYTHONPATH=$PYTHONPATH:/work


COPY ./config/.zshrc /tmp/.zshrc
RUN cat "/tmp/.zshrc" >> ~/.bashrc
WORKDIR /work