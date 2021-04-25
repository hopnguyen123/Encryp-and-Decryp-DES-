import CONVERT

Index_permuted1=[56,48,40,32,24,16,8,
				    0,57,49,41,33,25,17,
				    9,1,58,50,42,34,26,
				    18,10,2,59,51,43,35,
				    62,54,46,38,30,22,14,
				    6,61,53,45,37,29,21,
				    13,5,60,52,44,36,28,
				    20,12,4,27,19,11,3]

index_Permuted2=[13,16,10,23,0,4,2,27,
                      14,5,20,9,22,18,11,3,
                      25,7,15,6,26,19,12,1,
                      40,51,30,36,46,54,29,39,
                      50,44,32,47,43,48,38,55,
                      33,52,45,41,49,35,28,31]

def ShiftLeft_1(LIST):
    len_ = len(LIST)
    l_=LIST[0]
    for i in range(len_-1):
        LIST[i]=LIST[i+1]
    LIST[len_-1]=l_

def ShiftLeft_2(LIST):
    len_ = len(LIST)
    l0=LIST[0]
    l1=LIST[1]
    for i in range(len_-2):
        LIST[i]=LIST[i+2]
    LIST[len_-1]=l1
    LIST[len_-2]=l0

LIST_SHIFTLEFT=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]




def SUBKEY(key):
    #SUBKEY hoàn thành
    LIST_SUBKEY = []
    key_binary = CONVERT.hex_to_bin(key)

    Key_binary = list(key_binary)

    key_Permuted1 = []
    for i in Index_permuted1:
        key_Permuted1.append(Key_binary[i])

    # ROUND 1/16
    key_left = key_Permuted1[:28]
    key_right = key_Permuted1[28:]

    ROUND = 1
    ShiftLeft_1(key_left)
    ShiftLeft_1(key_right)

    list_p2 = []
    for i in key_left:
        list_p2.append(i)
    for i in key_right:
        list_p2.append(i)

    key_permuted2 = []
    for i in index_Permuted2:
        key_permuted2.append(list_p2[i])

    LIST_SUBKEY.append(key_permuted2)

    #	ROUND 2/16 -> 16/16
    ROUND = ROUND + 1

    while ROUND <= 16:
        if ROUND == 2 or ROUND == 9 or ROUND == 16:
            ShiftLeft_1(key_left)
            ShiftLeft_1(key_right)
        else:
            ShiftLeft_2(key_left)
            ShiftLeft_2(key_right)

        list_p2 = []
        for i in key_left:
            list_p2.append(i)
        for i in key_right:
            list_p2.append(i)

        key_permuted2 = []
        for i in index_Permuted2:
            key_permuted2.append(list_p2[i])

        LIST_SUBKEY.append(key_permuted2)

        ROUND = ROUND + 1

    #	XUÂT
    SUBKEY = []
    for i_ in LIST_SUBKEY:
        i_ = ''.join(i_)
        sub_int = []
        for i in i_:
            i = int(i)
            sub_int.append(i)
        SUBKEY.append(sub_int)
    return SUBKEY
    # for i in SUBKEY:
    # 	print(i)
    # print(len(SUBKEY))


# key="0123456789ABCDEF"
# t = SUBKEY(key)
# print(t)
# print(len(t))
# print(type(t))


