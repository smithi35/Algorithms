import random

def generate_array(size) :
	array = []
	
	for i in range(size):
		rando = random.randint(0,100)
		array.append(rando)
	
	return array
	
def qsort(first, last, array): 
	if (last - first > 1) :
		pivot = partition(first, last, array)
		# print("first = " + str(first) + ", last = " + str(last) + ", pivot = " + str(pivot))
		if (pivot - first == 1) :
			if (array[first] > array[pivot]) :
				swap(first, last, array)
		else :
			qsort(first, pivot, array)
			
		if (last - (pivot + 1) == 1) :
			if (array[pivot+1] > array[last]) :
				swap (pivot+1, last, array)
		else :
			qsort(pivot+1, last, array)
	
def partition(first, last, array):
	pivot_value = array[first]
	# partition the array so that everything less than pivot_value is to the left of it in the array,
	# and everything larger is to the right
	i = first+1
	j = last
	while (i < j) :
		while (i <= last and array[i] <= pivot_value ) :
			print("i = " + str(i) + ", pivot_value = " + str(pivot_value) + ", array[i] = " + str(array[i]))
			i = i + 1
		while (j >= first and array[j] > pivot_value ) :
			print("j = " + str(j) + ", pivot_value = " + str(pivot_value) + ", array[j] = " + str(array[j]))
			j = j - 1
		
		if (i < j) :
			swap(i, j, array)
	swap(j, first, array)
	return j
	
def swap (left, right, array) :
	temp = array[left]
	array[left] = array[right]
	array[right] = temp

def main() :
	array = generate_array(40)
	print(array)
	qsort(0, len(array)-1, array)
	print(array)
	
rando = random.seed()
main()