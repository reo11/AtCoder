from typing import List


def count_substring(string_list: List[str], sub_string: List[str]) -> int:
    """
    string_listに含まれる部分文字列sub_stringの個数を返す
    例: ["s", "t", "t", "r", "r"], ["s", "t", "r"] -> 4
    計算量: O(len(string_list) * len(sub_string))
    Args:
        string_list (List[str]): 検索対象の文字列
        sub_string (List[str]): 検索したい部分文字列
    Returns:
        int: 出現するsub_stringの個数
    """
    dp = [[0 for _ in range(len(sub_string) + 1)] for _ in range(len(string_list) + 1)]
    for i in range(1, len(string_list) + 1):
        for j in range(1, len(sub_string) + 1):
            if string_list[i - 1] == sub_string[j - 1]:
                if j == 1:
                    dp[i][j] = dp[i - 1][j] + 1
                else:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[len(string_list)][len(sub_string)]


if __name__ == "__main__":
    string_list = list(input())
    sub_string = list(input())
    print(count_substring(string_list, sub_string))
