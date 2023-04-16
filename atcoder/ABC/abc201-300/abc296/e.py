from collections import defaultdict


def strongly_connected_components(graph):
    """
    強連結成分分解を行う関数
    :param graph: ノードをキー、リスト形式の隣接ノードを値とする辞書
    :return: 各強連結成分のリストのリスト
    """
    index_counter = [0]
    stack = []
    lowlink = {}
    index = {}
    result = []

    def strongconnect(node):
        # ノードのインデックスを割り当て
        index[node] = index_counter[0]
        lowlink[node] = index_counter[0]
        index_counter[0] += 1
        stack.append(node)

        # 隣接ノードを探索
        try:
            for w in graph[node]:
                if w not in lowlink:
                    # 隣接ノードが未訪問の場合は再帰
                    strongconnect(w)
                    lowlink[node] = min(lowlink[node], lowlink[w])
                elif w in stack:
                    # 隣接ノードが訪問済みかつスタックにある場合は、
                    # そのノードが以前の強連結成分の一部であることがわかる
                    lowlink[node] = min(lowlink[node], index[w])

            # ルートノードが強連結成分に含まれるかどうかを判定する
            if lowlink[node] == index[node]:
                connected_component = []
                while True:
                    w = stack.pop()
                    connected_component.append(w)
                    if w == node:
                        break
                result.append(connected_component)
        except KeyError:
            pass

    for node in graph:
        if node not in lowlink:
            strongconnect(node)

    return result


n = int(input())
a = list(map(int, input().split()))
g = defaultdict(lambda: [])
for i in range(n):
    g[i].append(a[i] - 1)

group = strongly_connected_components(g)
print(group)
