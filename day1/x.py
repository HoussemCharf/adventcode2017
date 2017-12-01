with open('input.txt') as input_file:
	degits= input_file.read()
final_sum = 0
for i in xrange(len(degits)):
	j = (i+1) % len(degits)
	if degits[i] == degits[j]:
		final_sum += ord(degits[i]) - ord('0')
print final_sum
# Second half of the puzzle
final_sum = 0
for i in xrange(len(degits)):
	j = (i+len(degits)/2) % len(degits)
	if degits[i] == degits[j]:
		final_sum += ord(degits[i]) - ord('0')
print final_sum