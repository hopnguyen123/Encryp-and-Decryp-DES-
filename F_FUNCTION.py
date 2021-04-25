import S_BOX as SB

Index_P_box = [15,6,19,20,28,11,27,16,
               0,14,22,25,4,17,30,9,
               1,7,23,13,31,26,2,8,
               18,12,29,5,21,10,3,24]

index_Expansion=[31,0,1,2,3,4,
				3,4,5,6,7,8,
				7,8,9,10,11,12,
				11,12,13,14,15,16,
				15,16,17,18,19,20,
				19,20,21,22,23,24,
				23,24,25,26,27,28,
				27,28,29,30,31,0]


#r_0:  ['0', '1', '0', '1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '0', '1', '1', '1', '1', '0', '1', '0', '1', '0', '1', '0', '0', '1', '1', '1', '0', '0', '1']
# subkey_de[0]:  [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0]
def F_func1(r_0,subkey):

    # Expand R0 32bit->48bit
    r0_expansion = []
    for i in index_Expansion:
        r0_expansion.append(r_0[i])

    a = ''.join(r0_expansion)

    r0_int = []  # từ 48bit r0_str -> r0_int : để xor ở bước tiếp theo
    for i in a:
        i = int(i)
        r0_int.append(i)  # Có r0_int

    k1_int = []
    for i in subkey:
        k1_int.append(i)

    input_S_box = []
    for i in range(len(r0_int)):
    	x = r0_int[i] ^ k1_int[i]
    	input_S_box.append(x)

    S_box_str = SB.S_box(input_S_box)
    Output_S_box = list(S_box_str)

	# Permutation
    output_P_box = []
    for index in Index_P_box:
        output_P_box.append(Output_S_box[index])
    return output_P_box


def F_func2(r_in,subkey):
    # Mở rộng r_in
    r_in_expansion = []
    for i in index_Expansion:
        r_in_expansion.append(r_in[i])

    k_int = []
    for i in subkey:
        k_int.append(i)

    input_S_box = []
    for i in range(len(k_int)):
        x = r_in_expansion[i] ^ k_int[i]
        input_S_box.append(x)

    S_box_str = SB.S_box(input_S_box)
    Output_S_box = list(S_box_str)

    # Permutation
    output_P_box = []
    for index in Index_P_box:
        output_P_box.append(Output_S_box[index])
    return output_P_box



# r_in=  ['0', '1', '0', '1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '0', '1', '1', '1', '1', '0', '1', '0', '1', '0', '1', '0', '0', '1', '1', '1', '0', '0', '1']
# print(len(r_in))
# subkey =  [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0]
# x = F_func2(r_in,subkey)
# print(x)