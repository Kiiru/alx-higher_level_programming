#!/usr/bin/python3.8

if __name__ == "__main__":
    import hidden_4
    lt = dir(hidden_4)
    for i in lt:
        if not i.startswith("__"):
            print("{:s}".format(i))
