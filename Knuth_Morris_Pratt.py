def find_substring(string, pattern):
    # Driver
    lms = create_lms(pattern)

    return pattern_matched(string, pattern, lms)


def create_lms(sub):
    output = [0] * len(sub)
    i = 0

    for j in range(1, len(sub)):
        idx = 0
        if sub[i] == sub[j]:
            # idx = i = i + 1
            i += 1

        output[j] = idx

    return output


def pattern_matched(string, pattern, lms):
    p_idx = 0

    for s_idx in range(len(string)):
        if string[s_idx] == pattern[p_idx]:
            p_idx += 1
            if p_idx == len(pattern)-1:
                return True
        else:
            while string[s_idx] != pattern[p_idx]:
                if p_idx == 0:
                    break
                p_idx = lms[p_idx - 1]

    return False


string = [
    "a",
    "b",
    "c",
    "x",
    "a",
    "b",
    "c",
    "d",
    "a",
    "b",
    "x",
    "a",
    "b",
    "c",
    "d",
    "a",
    "b",
    "c",
    "d",
    "a",
    "b",
    "c",
    "y",
]
pattern = ["a", "b", "c", "d", "a", "b", "c", "y"]


print(find_substring(string, pattern))
