content = [line.strip('\n') for line in open('rosalind_gc.txt', 'r')]

raw = ''.join(content).split('>')

def find_max_gc(content):
	results = []
	for sample in content:
		if len(sample) < 1:
			pass
		else:
			title = sample[:13]
			seq = sample[13:]
			g_number = seq.count("G")
			c_number = seq.count("C")
			gc_totcount = g_number + c_number
			total = float(len(seq))
			results.append(((gc_totcount / total) * 100, title))
	results.sort(reverse=True)
	return results

ans = find_max_gc(raw)
print (ans[0][1])
print ("%s%%" % ans[0][0])
