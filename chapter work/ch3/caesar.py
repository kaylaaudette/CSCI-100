def rot13(msg):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in range(len(msg)):
        ch = msg[i] 
        if ch == ' ':
            result = result + ' '
        else:
            rotate = alphabet.index(ch) + 13
            if rotate < 26:
                result = result + alphabet[rotate]
            else:
                result = result + alphabet[rotate % 26]
    return result


print("------------------Q1-------------------")
print ( rot13('lbh ner n fhcre pbby pbqr oernxvat clguba cebtenzzre') )
print("---------------------------------------")