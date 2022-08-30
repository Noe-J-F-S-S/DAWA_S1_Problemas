def convercion(strl):
    if strl[-2:] == "AM" and strl[:2]=="12":
        return "00"+strl[2:-2]
    elif strl[-2:]=="AM":
        return strl[:-2]
    elif strl[-2:]=="PM" and strl[:2] =="12":
        return strl[:-2]
    else:
        return str(int(strl[:2])+12)+strl[2:8]

print(convercion("09:45:34 AM"))
