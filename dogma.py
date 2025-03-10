def tm(seq):
	counts = [seq.count('A'), seq.count('C'), seq.count('G'), seq.count('T')]
	if len(seq) <= 13: return (counts[0] + counts[3]) * 2 + (counts[1] + counts[2]) * 4
	else:		return (64.9 + 41 * (counts[1] + counts[2] - 16.4) / 
				(counts[0] + counts[1] + counts[2] + counts[3]))
