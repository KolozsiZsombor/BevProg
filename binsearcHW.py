def main():
    A = [2, 5, 6, 8, 13, 32, 42, 50, 53, 62, 66, 70, 80, 89, 91]
    N = len(A)
    r = 0
    bottom, top = 0, N - 1
    search = 70
    out = None
    while bottom <= top:
        r += 1
        k = (top + bottom) // 2
        if search < A[k]:
            top = k - 1
        elif search > A[k]:
            bottom = k + 1
        else:
            out = r, bottom, top
            break
    else:
        out = False

    return out


if __name__ == "__main__":
    print(main())
