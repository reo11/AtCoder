# AtCoder Env
FROM python:3.4.3

CMD echo 'Install lib for atcoder'
# RUN apt update && apt install -y --no-install-recommends build-essential sudo
# RUN apt-get install -y python-scikits-learn
# RUN apt-get install -y  python3-numpy
# RUN apt-get install -y python3-scipy

RUN pip install -U pip
RUN pip install scikit-learn
# scikit-learnで全部入る
# RUN pip install numpy
# RUN pip install scipy