
from random import randint
from time import time



# function: Pivot_Leftmost

# parameters: any list

# returns: the first value in the list

# purpose: find the first value of the list to use as a pivot

def Pivot_Leftmost(List):
    return List[0]

# ---------------------------------------------------------------------------
# function: Pivot_Best_of_3

# parameters: any list with at least 3 values

# returns: a pivot using best of 3 method

# purpose: find a pivot using best of 3 method, which picks 3 evenly distributed
# values and finds the median

def Pivot_Best_of_3(List):

    # finds the 3 values to use
    n = len(List)- 1
    start = 0
    mid = n//2

    #print("values: ", List[start], List[mid], List[n])

    # since it is only 3 values, removes the highest and lowest
    myList=[List[start], List[mid], List[n]]
    myList.remove(max(myList))
    myList.remove(min(myList))

    # sets the remaining value to a variable
    pivot= myList[0]
    
    
    return pivot

# ---------------------------------------------------------------------------
# function: Pivot_Ninther

# parameters: any list with at least 9 values

# returns: a pivot using the Ninther method

# purpose: find a pivot using Ninther method which picks the median
# of 3 sets of evenly distributed medians

def Pivot_Ninther(List):

    # creates a value to use to find the distance between each value to find the 9 numbers
    dist = len(List)//9

    # creates a group of the first 3 evenly distributed numbers
    group1 = [List[0], List[dist], List[dist*2]]

#    group1_start = [List[0], List[dist], List[dist*2]]

    # removes the top and bottom value of each set to find the median of the set
    
    group1.remove(max(group1))
    group1.remove(min(group1))

#    print("group 1: ", group1_start, "median 1: ", group1)
    
    group2 = [List[dist*3], List[dist*4], List[dist*5]]

#    group2_start = [List[dist*3], List[dist*4], List[dist*5]]

    group2.remove(max(group2))
    group2.remove(min(group2))

#    print("group 2: ", group2_start, "median 2: ", group2)
    
    group3 = [List[dist*6], List[dist*7], List[dist*8]]

##    group3_start= [List[dist*6], List[dist*7], List[dist*8]]
    
    group3.remove(max(group3))
    group3.remove(min(group3))

##    print("group 3: ", group3_start, "median 3: ", group3)
##    print("all medians: ", group1, group2, group3)

    # creates a list of the medians of the 3 groups
    medianmed = group1 + group2 + group3
    
    medianmed.remove(max(medianmed))
    medianmed.remove(min(medianmed))

    # returns the remaining value which is the median of the medians
    return medianmed[0]

# ---------------------------------------------------------------------

def quick_sort_bo3(List):

    # if the list is less than 2 values
    if len(List) <2:

        # return it as is
        return List

  
    # finds a pivot using best of 3 method
    pivot = Pivot_Best_of_3(List)

    # print("pivot:",pivot)

    # makes 3 empty lists for the left and right bins and the pivots
    leftList=[]
    rightList=[]
    pivotList=[]

    # for each value in the list, assigns it to a bin using its size compared to the pivot
    for val in List:
        
        if val < pivot:
            
            leftList.append(val)
            
        elif val== pivot:
            
            pivotList.append(val)
            
        
        else:
            rightList.append(val)
            
    #print("Left List:",leftList)
    #print("Right List:",rightList)
    #print("")

    # recursively runs using the left and right bins
    q= quick_sort_bo3(leftList)
   
    w= quick_sort_bo3(rightList)
    
    # returns a sorted list or sorted bin
    return q+ pivotList+w

# ----------------------------------------------------------------------------

# parameters: an unsorted List

# returns: a sorted List or List segment to previous recursions

# purpose: sort a list recursively by dividing the list into bins and
# recombining while finding pivots using the leftmost item in the list

def quick_sort_leftmost(List):

    # if the list is one or fewer values, return as is
    if len(List) <2:
        
        return List

  
    # finds the pivot using leftmost value in list
    pivot = Pivot_Leftmost(List)

    #print("pivot",pivot)

    # creates 3 empty lists for the bins and pivots
    leftList=[]
    rightList=[]
    pivotList=[]

    # moves values into left or right bins based on whether the value is larger
    # or smaller than the pivot or if it is the same as the pivot
    for val in List:

        if val < pivot:

            leftList.append(val)
            
        elif val== pivot:
            
            pivotList.append(val)
            
        
        else:
            rightList.append(val)
   # print("Left list",leftList)
   # print("Right List",rightList)

    # uses the best of the method for other recursions
    q= quick_sort_bo3(leftList)
   
    w= quick_sort_bo3(rightList)
    
   # print("left bin: ", q, "right bin:", w)

    # returns sorted list
    return q+ pivotList+w

# ----------------------------------------------------------------------------

# parameters: an unsorted list ; a pivot found using Ninther method

# returns: a sorted list

# purpose: sorts a list recursively and finds pivots using Ninther method

def quick_sort_ninther(List, Pivot):

    # if the list has 1 or fewer values
    if len(List) <2:

        # return the list as is
        return List

    # creates 3 empty lists to hold bins and pivots
    leftList=[]
    rightList=[]
    pivotList=[]

    # for each
    for val in List:

        # if value is smaller than the pivot
        if val < Pivot:

            # put it into the left bin
            leftList.append(val)

        # if the value is the same as the pivot
        elif val== Pivot:

            # move it into the pivot list
            pivotList.append(val)
            
        
        else:

            # if the value is larger than the pivot, put it in the right bin
            rightList.append(val)

    # recursively uses the function on the left and right bins
    q= quick_sort_bo3(leftList)
   
    w= quick_sort_bo3(rightList)
    
   # print("left bin: ", q, "right bin:", w)

    # returns the sorted list
    return q+ pivotList+w

# ----------------------------------------------------------------------------

# parameters: an unsorted list

# returns: a sorted list

# purpose: sorts by checking every value in an unsorted list and comparing
#          it to the last value in a sorted list
def insertion_sort(List):


    n = len(List)-1
    sortedList = []
    # repeats for as long as the list is
    for i in range(1, n):

        # picks the value to compare
        value = List[i]

        # compares the value with every number currently in the list
        for j in range(len(sortedList)):

            #if the value is lower than a value, inserts it before the current list value
            if value < sortedList[j]:

                sortedList.insert(j, value)
                
                break

            # if it's greater than any value in the list, places it at the end
            elif value >= sortedList[len(sortedList)-1]:
                
                sortedList.append(value)

                break
            
    # returns the sorted list  
    return sortedList


# ----------------------------------------------------------------------------------------------------


n= int(input("enter list size: "))

# creates a random list of specified length using randint function
randList=[]
for i in range(1, n+1):
    randList.append(randint(1,100000))
print("List Length", len(randList))


#creates a sorted list of specified length
sortedList = []
for i in range(1, n+1):
    sortedList.append(i)

# timing code sets

start_time1 = time()
for rep1 in range(10000):
    leftmost=quick_sort_leftmost(randList)
stop_time1 = time()

total_time1 = stop_time1 - start_time1
C = total_time1/(10000*n**2)

print("Unsorted List")
print("\nLeftmost Quicksort")
print("single time:",total_time1/10000)
print("est C:", C)
print("\n")

start_time2 = time()

for rep1 in range(10000):
    bo3=quick_sort_bo3(randList)

stop_time2 = time()

total_time2 = stop_time2 - start_time2
C = total_time2/(10000*n**2)

print("Best of 3 Quicksort")
print("single time:",total_time2/10000)
print("est C:", C)
print("\n")

start_time3 = time()
nintherPivot = Pivot_Ninther(randList)
for rep1 in range(10000):
    ninthersort=quick_sort_ninther(randList, nintherPivot)
stop_time3 = time()
total_time3 = stop_time3 - start_time3
C = total_time3/(10000*n**2)

print("Ninther Quicksort")
print("single time:",total_time3/10000)
print("est C:", C)
print("\n")

start_time4 = time()

for rep1 in range(10000):
    insort= insertion_sort(randList)

stop_time4 = time()
total_time4 = stop_time4 - start_time4
C = total_time4/(10000*n**2)

print("Insertion Sort")
print("single time:",total_time4/10000)
print("est C:", C)
print("\n\n")

# ---------------------------------------------------------
# sorted list
start_time_1 = time()

for rep1 in range(10000):
    sortedlist=quick_sort_leftmost(sortedList)
    
stop_time_1 = time()
total_time_1 = stop_time_1 - start_time_1
C = total_time_1/(10000*n**2)

print("SORTED LIST")
print("\nLeftmost Quicksort")
print("single time:",total_time_1/10000)
print("est C:", C)
print("\n")

start_time_2 = time()

for rep1 in range(10000):
    bo3sorted=quick_sort_bo3(sortedList)
    
stop_time_2 = time()
total_time_2 = stop_time_2 - start_time_2
C = total_time_2/(10000*n**2)

print("Best of 3 Quicksort")
print("single time:",total_time_2/10000)
print("est C:", C)
print("\n")

start_time_3 = time()
nintherPivot = Pivot_Ninther(sortedList)
for rep1 in range(10000):
    quick_sort_ninther(sortedList, nintherPivot)
    
stop_time_3 = time()
total_time_3 = stop_time_3 - start_time_3
C = total_time_3/(10000*n**2)

print("Ninther Quicksort")
print("single time:",total_time_3/10000)
print("est C:", C)
print("\n")

start_time_4 = time()
for rep1 in range(10000):
    insorted=insertion_sort(sortedList)
    
stop_time_4 = time()
total_time_4 = stop_time_4 - start_time_4
C = total_time_4 /(10000*n**2)

print("Insertion Sort")
print("single time:",total_time_4/10000)
print("est C:", C)
print("\n")



