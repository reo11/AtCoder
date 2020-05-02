# AtCoder
AtCoderやる

## 新環境のAtCoder用Dockerfile
https://docs.google.com/spreadsheets/d/1PmsqufkF3wjKN6g1L0STS80yP4a6u-VdGiEv5uOHe0M/edit#gid=1059691052
から適当に取ってきて動くようにした。
dockerとdocker-composeがあれば動くはず。

### buildとか
バックグラウンドで実行します。
作業する時はdocker内で。
```
docker-compose up --build -d
docker exec -it atcoder bash
```

### aliasについて
とりあえず公式で使われてるコマンドのaliasを`.zshrc`に書いたので、適当にやれば使えるはず。
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
