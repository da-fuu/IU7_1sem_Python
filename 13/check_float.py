def main(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return 0 <= float(s) <= 1
