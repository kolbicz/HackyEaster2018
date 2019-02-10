
list = ['CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK', 'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 
		'DJ', 'DQ', 'DK', 'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK', 'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 
		'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'JA', 'JB']

key = ['D8', 'S3', 'D7', 'D3', 'C2', 'S5', 'DA', 'C6', 'S7', 'D6', 'JA', 'DK', 'HQ', 'SJ', 'CJ', 'H7', 'H3', 'H9', 'S9', 'S8', 'C9', 'SA', 'H4', 
		'C8', 'C3', 'HK', 'HA', 'S6', 'H6', 'S10', 'SK', 'CA', 'D10', 'DQ', 'CQ', 'JB', 'SQ', 'S4', 'D9', 'S2', 'C5', 'HJ', 'H10', 'C4', 'C10', 
		'D5', 'H8', 'H2', 'D2', 'DJ', 'C7', 'CK', 'H5', 'D4']

num = ""

for k in key:
	num += str(list.index(k)+1)+","
	
print num[:-1]