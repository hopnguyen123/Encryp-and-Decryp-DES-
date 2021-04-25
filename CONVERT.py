def bin_to_ascii(input_str):    #bin -> ascii, nhưng đầu vào là type(str) nhiều 0,1  - đầu ra là ascii
    index_cut=[]
    n_ = len(input_str)
    for i in range(0,n_,8):
        index_cut.append(i)
    output=""
    for index in index_cut:
        l1 = []
        subindex = input_str[index:index+64]
        for i in subindex:
            i = int(i)
            l1.append(i)
        x = l1[0] * (2 ** 7) + l1[1] * (2 ** 6) + l1[2] * (2 ** 5) + l1[3] * (2 ** 4) + l1[4] * (2 ** 3) + l1[5] * (2 ** 2) + l1[6] * (2) + l1[7]
        chr_ =chr(x)
        output+=chr_

    return output

def dec_to_bin(n):  #Đầu vào là decima (hệ 10), đầu ra là type(string) dưới dạng 0,1..
    x = bin(n)[2:]
    k = str(x)
    n = len(k)
    while n<4:
        k = "0"+k
        n+=1
    return k

def hex_to_bin(key):    #Đầu vào là type(string) dưới dạng 0,1,..,E,F   -   đầu ra là type(string) dưới dạng bin 0,1..
    key_binary = ""
    # Chuyển Key HEX -> BINARY
    for i in key:
        if i == 'A' or i == 'a':
            key_binary += "1010"
        elif i == 'B' or i == 'b':
            key_binary += "1011"
        elif i == 'C' or i == 'c':
            key_binary += "1100"
        elif i == 'D' or i == 'd':
            key_binary += "1101"
        elif i == 'E' or i == 'e':
            key_binary += "1110"
        elif i == 'F' or i == 'f':
            key_binary += "1111"
        else:
            key_binary += bin(ord(i))[4:]
    return key_binary
#
# key = "0123456789ABCDEF"
# x = hex_to_bin(key)
# print(x)
# print(type(x))