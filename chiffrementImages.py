def xor(a,b):
    if bool(a) != bool(b):
        return True
    else:
        return False

def conv(c):
    return str(bin(c)[2:].zfill(8))

print(conv(0))

