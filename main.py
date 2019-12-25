"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""


"""
def merge(lst):
  #Store merged lists
  newlst = []
  for i in range(len(lst) - 1):
    #Tail of first element >= head of second
    if (i < len(lst) - 1) and (lst[i][1] >= lst[i+1][0]):
      #Create interval with first el head and second el tail
      newlst += [lst[i][0],lst[i+1][1]]
    else:
      #Get a visualization of where the condition fails
      print("Passing on " + str(lst[i]))
      del lst[i]
      print(lst[i])
      newlst += lst[i]
  return newlst

print(merge([[1,3],[2,6],[8,10],[15,18]]))

test = [[1,3],[2,6],[8,10],[15,18]]
"""

def merge(lst):
  newlst = []
  for i in lst:
    #Create list using first el; on future loops, check tail of el against head of next el. If Tail[before] < head[cur], no interval, append cur
    if not newlst or newlst[-1][-1] < i[0]:
      print("appending " + str(i))
      newlst.append(i)
    #Check tail of el against tail of cur; 
    elif newlst[-1][-1] < i[-1]:
      print("Replacing " + str(newlst[-1][-1]) + " with " + str(i[-1]))
      newlst[-1][-1] = i[-1]
  return newlst

print(merge([[1,3],[2,6],[8,10],[15,18]]))

