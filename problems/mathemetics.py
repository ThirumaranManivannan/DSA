# given number x find no of difits in it if x = 46567, ans = 5 x > 0

def countDigits(x):
	count = 0
	while x > 0:
		x = int(x / 10)
		count += 1
	return count


# print(countDigits(2345))  # time O(d) digits space O(1)

# Given number n palindrome or not

def isPalindrome(n):
	rev = 0
	temp = n
	while temp > 0:
		ld = temp % 10
		rev = rev * 10 + ld
		temp = int(temp/10)
	return rev == n


# print(isPalindrome(34543))  # time O(d) space O(1)

# Factorial of a given number iterative approach

def factorial(n):
	if n < 2:
		return 0
	fact = 1
	for i in range(1, n + 1):
		fact = fact * i
	return fact

# time O(n) space O(1)


def factorialRecursive(n):
	if n < 2:
		return 0
	return n * factorial(n-1)


# print(factorialRecursive(4))  # time O(n) space O(n) since function stack proportional to n

# count of trailing zero's on factorial of an number

def countTrailingZeros(n):
	fact = factorial(n)
	print(fact)
	count = 0
	while fact % 10 == 0:
		fact = int(fact/10)
		count += 1
	return count


print(countTrailingZeros(10))  # time O(n) space O(1)
