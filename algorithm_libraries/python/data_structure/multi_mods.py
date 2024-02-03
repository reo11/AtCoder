hash_keys = [2**13 - 1, 2**17 - 1, 2**19 - 1, 2**31 - 1]

def multi_mods(x, hash_keys):
    mods = []
    for key in hash_keys:
        mods.append(x % key)
    return mods

if __name__ == "__main__":
    pass
