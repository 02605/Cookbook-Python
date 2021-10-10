

# 递归
def sum(items):
    head, *tail = items
    print(head, tail)
    return head + sum(tail) if tail else head


if __name__ == '__main__':

    print(sum([10, 20]))
