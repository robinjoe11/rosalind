from Bio import SeqIO
import numpy as np




seq_name, seq_string = [], []
with open ("rosalind_cons.txt",'r') as fa:
    for seq_record  in SeqIO.parse(fa,'fasta'):
        seq_name.append(str(seq_record.name))
        seq_string.append(str(seq_record.seq))

seq_len = len(seq_string)
str_len = len(seq_string[0])

symbol = ["A", "C", "G", "T"]
consensus_string = ""
profile = np.zeros(shape=(4, str_len), dtype=int)

for c in range(str_len):
    position_symbl = [s[c] for s in seq_string]
    most_common_symbl = max(position_symbl, key=position_symbl.count)
    consensus_string += most_common_symbl
    for r in range(len(symbol)):
        profile[r][c] = position_symbl.count(symbol[r])
    
print(consensus_string)
for i in range(len(symbol)):
    print("{}: {}".format(symbol[i], " ".join([str(j) for j in profile[i]])))