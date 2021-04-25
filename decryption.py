import CONVERT 			#Module để convert (bin,hex,dec,ascii)
import SUBKEY as SK		#Module sinh ra khoá con
import F_FUNCTION as F_	#Module hàm F


index_Initial_permutation=[57,49,41,33,25,17,9,1,
              				59,51,43,35,27,19,11,3,
              				61,53,45,37,29,21,13,5,
              				63,55,47,39,31,23,15,7,
              				56,48,40,32,24,16,8,0,
              				58,50,42,34,26,18,10,2,
              				60,52,44,36,28,20,12,4,
              				62,54,46,38,30,22,14,6]

index_final_permutation=[39,7,47,15,55,23,63,31,
						 38,6,46,14,54,22,62,30,
						 37,5,45,13,53,21,61,29,
						 36,4,44,12,52,20,60,28,
						 35,3,43,11,51,19,59,27,
						 34,2,42,10,50,18,58,26,
						 33,1,41,9,49,17,57,25,
						 32,0,40,8,48,16,56,24]

#	--------------------- SINH KHOÁ ------------------------------------
# #Nhập Key đầu vào 64bit, hệ HEX(16)
# key="0123456789ABCDEF"
print("Nhap key hệ HEX: ",end = ' ')
key = input()
SUB_KEY = SK.SUBKEY(key)

SUBKEY_Decryption=[]
n_ = len(SUB_KEY)-1
while n_ >=0:
	SUBKEY_Decryption.append(SUB_KEY[n_])
	n_-=1

#	------------------------ CIPHERTEXT	-------------------------------
# ciphertext_bin="10010100001111010001001100101010011100110000110101110000000111101011101111100001000111000010001011001111010000101111110001101100"
# print("Ciphertext_bin: ",ciphertext_bin)
print("Nhap Ciphertext_bin: ",end=' ')
ciphertext_bin = input()
PLAINTEXT_BIN=[]
LIST_CIPHERTEXT=[]

#	cắt ciphertext
index_cut=[]
n_len = len(ciphertext_bin)
for i in range(0,n_len,64):
    index_cut.append(i)
for i in index_cut:
    l=list(ciphertext_bin[i:i+64])
    LIST_CIPHERTEXT.append(l)

#Mỗi ciphertext (64bit) sẽ được xử lý lần lượt
for hasaki in LIST_CIPHERTEXT:

	# Intial_Permuation
	Intial_Permutation = []
	for i in index_Initial_permutation:
		Intial_Permutation.append(hasaki[i])

	# ------------------------------------------------------

	# ROUND 1/16

	# chia thành 2 phần
	l_0 = Intial_Permutation[:32]
	r_0 = Intial_Permutation[32:]

	l_1 = r_0
	l1_int = []
	for i in l_1:  # Có l_1
		i_ = int(i)
		l1_int.append(i_)

	#	Hàm F
	output_P_box=F_.F_func1(r_0,SUBKEY_Decryption[0])

	#	Hàm XOR
	l0_int = []  			# từ 48bit r0_str -> r0_int : để xor ở bước tiếp theo
	a = ''.join(l_0)
	for i in a:
		i = int(i)
		l0_int.append(i)  	# Có l0_int

	input_xor = []
	for i in output_P_box:
		i_ = int(i)
		input_xor.append(i_)

	r_1 = []
	for i in range(len(l0_int)):
		x = l0_int[i] ^ input_xor[i]
		r_1.append(x)


	# ROUND 2/16 -> 16/16 -------------------------------------------------
	l_in = []
	for i in l1_int:
		l_in.append(i)
	r_in = []
	for i in r_1:
		r_in.append(i)

	ROUND_ = 2

	while ROUND_ <= 16:
		l_out = []
		r_out = []
		for i in r_in:
			l_out.append(i)  # Có l_out

		#	F_Function
		output_P_box = F_.F_func2(r_in,SUBKEY_Decryption[ROUND_-1])

		# Xor sau P_box
		input_xor = []
		for i in output_P_box:
			i_ = int(i)
			input_xor.append(i_)

		for i in range(len(l_in)):
			x = l_in[i] ^ input_xor[i]
			r_out.append(x)  # Có r_out

		l_in = []
		for i in l_out:
			l_in.append(i)
		r_in = []
		for i in r_out:
			r_in.append(i)

		ROUND_ += 1

	# ---------------------- kết thúc 	------------

	input_final_Permuation = []
	for i in r_out:
		input_final_Permuation.append(i)
	for i in l_out:
		input_final_Permuation.append(i)

	PLAINTEXT = []
	for i in index_final_permutation:
		PLAINTEXT.append(input_final_Permuation[i])

	a = []
	for i in PLAINTEXT:
		i = str(i)
		a.append(i)
	x = ''.join(a)
	# print(x)
	PLAINTEXT_BIN.append(x)

k = ''.join(PLAINTEXT_BIN)
j = CONVERT.bin_to_ascii(k)
print("plaintext: ",j)





