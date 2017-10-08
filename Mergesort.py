def generate_array(array) :
    for i in range(0, 10) :
        array.append(i % 7)
        
def print_array(array, start, end) :
    output = ""
    for i in range(start, end) :
        output = output + str(array[i]) + " "
    print(output)

def swap(array, left, right) :
    temp = array[left]
    array[left] = array[right]
    array[right] = temp

def merge(array, left, right, end) :
    first = array[left:right]
    second = array[right:end]
    
    i = 0
    j = 0
    while (left < end) and (i < len(first)) and (j < len(second)) :
        if first[i] <= second[j] :
            array[left] = first[i]
            i = i + 1
        else :
            array[left] = second[j]
            j = j + 1
        left = left + 1
        
    while i < len(first) :
        array[left] = first[i]
        i = i + 1
        left = left + 1
        
    while j < len(second) : 
        array[left] = second[j]
        j = j + 1
        left = left + 1
    
def merge_sort(array, start, end) :
    difference = end - start
    print("difference = " + str(difference))
    print("start =  " + str(start) + ", end = " + str(end))
    
    if (end - start > 2) :
        mid = int((end + start) / 2)
        merge_sort(array, start, mid)
        merge_sort(array, mid, end)
        merge(array, start, mid, end)
    else :
        if (array[start] > array[end-1]) :
            swap(array, start, end-1)

def main() :
    array = []
    generate_array(array)
    print_array(array, 0, len(array))
    merge_sort(array, 0, len(array))
    print_array(array, 0, len(array))

main()