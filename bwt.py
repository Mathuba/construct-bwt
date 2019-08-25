# python3
import sys

def build_suffix_array(text):
    t_len = len(text)
    result = [0] * t_len

    suffixes = [ (i, text[i:]) for i in range(t_len)]
    suffixes.sort(key=lambda x: x[1])

    for i, _ in enumerate(suffixes):
        result[i] = suffixes[i][0]

    return result

def BWT(text):
    suf_array = build_suffix_array(text)
    return "".join(text[num_value-1] for num_value in suf_array )

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))