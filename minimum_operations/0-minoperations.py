#!/usr/bin/python3


def minOperations(n):


if not isinstance(n,int) or n < 2:
	return 0

ops = 0
factor = 2
while factor * factor <= n:
	while n % factor == 0:
		ops += factor
		n //= factor
	factor +1
if n > 1:
	ops += n
return ops
