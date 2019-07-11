
def quantosobra(start, end):
    for numb in range(start, end):
        message = ""
        is_quantosobra = False

        if numb % 5 == 0:
            message = "Quanto"
            is_quantosobra = True

        if numb % 3 == 0:
            message += "Sobra"
            is_quantosobra = True

        if not is_quantosobra:
            message = str(numb)

        yield message


if __name__ == "__main__":
    [print(m) for m in quantosobra(1, 101)]
