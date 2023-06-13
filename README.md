[![Test & Lint](https://github.com/reo11/AtCoder/actions/workflows/docker-image.yml/badge.svg)](https://github.com/reo11/AtCoder/actions/workflows/docker-image.yml)

# AtCoder
AtCoderのコードを置いておく場所

## 新環境のAtCoder用Dockerfile
[AtCoder 2019/7 Language Update](https://docs.google.com/spreadsheets/d/1PmsqufkF3wjKN6g1L0STS80yP4a6u-VdGiEv5uOHe0M/edit#gid=1059691052)
から適当に取ってきて動くようにした。
dockerが入っていれば動くはず．

### build
makeコマンドでコンテナを出入りできます。
```
make
```

WSL環境で`ERROR [internal] load metadata`が出る場合、ubuntuをpullした後makeすると良い。
```
docker pull ubuntu:18.04
```

### alias
とりあえず公式で使われてるコマンドのaliasを`config/.zshrc`に書いたので、適当にやれば使えるはず。
```
python a.py
pypy a.py
cpp a.cpp
```

### online jundge toolsを使う
```
login_atcoder
submit_pypy a
submit_python a
submit_cpp a
```

### python標準ライブラリの計算量
https://qiita.com/bee2/items/4ab87d05cc03d53e19f9

aaaa