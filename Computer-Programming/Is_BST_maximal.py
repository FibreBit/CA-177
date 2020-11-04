def is_maximal(bst):
	a = bst.count()
	n = 1
	i = 0
	while n < a:
		n = n + 2 ** (i + 1)
		i += 1
	if n == a and i == bst.height() - 1:
		return True
	return False
