# Binary search
import math


def binarySearch(arr, start, end, val):
	print('steps')
	if start > end:
		return -1
	mid = int(start + (end - start) / 2)  # to avoid integer overflow
	if arr[mid] == val:
		return mid
	elif arr[mid] < val:
		return binarySearch(arr, mid + 1, end, val)
	else:
		return binarySearch(arr, start, mid - 1, val)


def binarySearchIteration(arr, val):
	end = len(arr) - 1
	start = 0
	while start <= end:
		print("steps")
		mid = int(start + (end - start) / 2)  # to avoid integer overflow
		if arr[mid] == val:
			return mid
		elif arr[mid] < val:
			start = mid + 1
		else:
			end = mid - 1
	return -1


# print(binarySearchIteration([2, 7, 10, 45, 89, 567], 10))

# Jump search

def jumpSearch(arr, length, val):
	step = int(math.sqrt(length))
	prev_step = 0
	while step < length and arr[step] < val:
		print("steps taken")
		prev_step = step
		step += int(math.sqrt(length))
		if prev_step >= length - 1:
			return -1
	while prev_step < length:
		print("2nd steps taken")
		if arr[prev_step] == val:
			return prev_step
		prev_step += 1
		if prev_step >= length:
			return -1
	return -1


# print(jumpSearch([2, 7, 10, 45, 89, 567, 568, 601, 701, 801, 90, 1001], 12, 1001))

def exponentialSearch(arr, val):
	end = len(arr)
	if arr[0] == val:
		return 0
	i = 1
	while i < end and arr[i] <= val:
		print("exp steps")
		i *= 2
	return binarySearch(arr, int(i / 2), min(i, end), val)

# print(exponentialSearch([2, 7, 10, 45, 89, 567, 568, 601, 701, 801, 90, 1001], 1001))
