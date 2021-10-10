self_str = "610324199902230035RX"

NAME = slice(-2, len(self_str))
BIR = slice(6, 14)

print(self_str[NAME])
print(self_str[BIR])
print(NAME.start, NAME.stop, NAME.step)