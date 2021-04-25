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


#	-----		KEY			------
print("Nhap key hệ HEX: ",end = ' ')
key = input()
SUB_KEY = SK.SUBKEY(key)


#	-----		PLAINTEXT		-----
print("Nhap Plaintext: ",end =' ')		#PlainText (ASCII) -> Binary
plaintext = input()

Plaintext_hex=""
Plaintext_bin=""

for i in plaintext:
	Plaintext_hex+=hex(ord(i))[2:]
print(Plaintext_hex)

Plaintext_bin = CONVERT.hex_to_bin(Plaintext_hex)


#	----	MODE	EBC 	-----
demkitu_plaintext=len(plaintext)
x = demkitu_plaintext%8
y = demkitu_plaintext//8

if x!=0:
    sktcanthem= (y+1)*8 - demkitu_plaintext
    sokitucanthem = sktcanthem - 1
    print(sokitucanthem)
    chuoithem = "10000000"
    for i in range(sokitucanthem):
        chuoithem += "00000000"
    Plaintext_bin += chuoithem

LIST_PLAINTEXT=[]
LIST_CIPHERTEXT=[]


#Cắt PLAINTEXT ban đầu thành nhiều chuỗi 64bit
index_cut=[]
n_len = len(Plaintext_bin)
for i in range(0,n_len,64):
    index_cut.append(i)
for i in index_cut:
    l=list(Plaintext_bin[i:i+64])
    LIST_PLAINTEXT.append(l)


#Encryption mỗi đoạn 64bit của Plaintext
for hasaki in LIST_PLAINTEXT:
	Intial_Permutation = []				#Hoán vị lần đầu của từng khối Plaintext
	for i in index_Initial_permutation:
		Intial_Permutation.append(hasaki[i])

	# 			ROUND 1/16

	# Chia 2 phần		- LEFT - | - RIGHT -
	l_0 = Intial_Permutation[:32]
	r_0 = Intial_Permutation[32:]
	l_1 = r_0

	#Chuyển các kí tự trong l_1 từ string -> int
	l1_int = []
	for i in l_1:  											# Có l1_int
		i_ = int(i)
		l1_int.append(i_)


	# Chuyển l_0 tù string -> int
	l0_int = []
	a = ''.join(l_0)
	for i in a:
		i = int(i)
		l0_int.append(i)  # Có l0_int	(32bit) (Để XOR với output_P_box)	=> r1


	#		Hàm F
	output_P_box=F_.F_func1(r_0,SUB_KEY[0])


	# 		Xor sau P_box của ROUND 1/16
	input_xor = []
	for i in output_P_box:
		i_ = int(i)
		input_xor.append(i_)

	r_1 = []
	for i in range(len(l0_int)):
		x = l0_int[i] ^ input_xor[i]
		r_1.append(x)


	# 			ROUND 2/16 -> 16/16
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
			l_out.append(i)  			# Có l_out (của từng ROUND)

		#		Hàm F
		output_P_box = F_.F_func2(r_in, SUB_KEY[ROUND_ - 1])

		# Xor sau P_box
		input_xor = []					#input của xor = output của P_box
		for i in output_P_box:
			i_ = int(i)
			input_xor.append(i_)

		for i in range(len(l_in)):
			x = l_in[i] ^ input_xor[i]
			r_out.append(x)  				# Có r_out (của từng ROUND)

		#l_in và r_in của ROUND tiếp theo
		l_in = []
		for i in l_out:
			l_in.append(i)
		r_in = []
		for i in r_out:
			r_in.append(i)

		ROUND_ += 1
	# ----------------------------------

	# SAU 16 ROUND -> có l_out và r_out
	input_final_Permuation = []
	for i in r_out:
		input_final_Permuation.append(i)
	for i in l_out:
		input_final_Permuation.append(i)

	#CIPHERTEXT = hoán vị cuối cùng
	CIPHERTEXT = []
	for i in index_final_permutation:
		CIPHERTEXT.append(input_final_Permuation[i])

	#Chuyển CIPHERTEXT (list -> string)
	k = []
	for i in CIPHERTEXT:
		x = str(i)
		k.append(x)
	k = ''.join(k)

	LIST_CIPHERTEXT.append(k)

#----------- 	KẾT QUẢ 	----------------
print(LIST_CIPHERTEXT)
OUTPUT_CIPHER = ''.join(LIST_CIPHERTEXT)
print(OUTPUT_CIPHER)






