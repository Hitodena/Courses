def to_str(n, base): # 254, 16
    convert = "0123456789ABCDEF"
    if n < base:
        return convert[n] # convert[2] = 2
    else:
        return to_str(n // base, base) + convert[n % base] #convert[14] = 'E'
    

print(to_str(254, 16))