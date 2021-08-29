# merge sort algorithm

# merge method in place

def merge(arr, left, rigt):
	left_idx = right_idx = actual_idx = 0
	while left_idx < len(left) and right_idx < len(rigt):
		if left[left_idx] < rigt[right_idx]:
			arr[actual_idx] = left[left_idx]
			left_idx += 1
			actual_idx += 1
		else:
			arr[actual_idx] = rigt[right_idx]
			right_idx += 1
			actual_idx += 1
	while left_idx < left:
		arr[actual_idx] = left[left_idx]
		actual_idx += 1
		left_idx += 1
		
