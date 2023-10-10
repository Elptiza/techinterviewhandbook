# Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
# Example 1:
# Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
# Output: [1, 1, 2, 3, 4, 4]
#
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
#
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]
#
# Constraints:
# The number of nodes in both lists is in the range[0, 50]. -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non - decreasing order.

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    result = []
    i_list1 = 0
    i_list2 = 0
    while i_list1 < len(list1) and i_list2 < len(list2):
        print(i_list1,i_list2)
        if list1[i_list1] < list2[i_list2] :
            result.append(list1[i_list1])
            i_list1 += 1
        else :
            result.append(list2[i_list2])
            i_list2 += 1
    if i_list1 < len(list1) :
        result = result + list1[i_list1:]
    if i_list2 < len(list2) :
        result = result + list2[i_list2:]
    print(result)


# list1 = [1, 2, 4]
# list2 = [1, 3, 4]
# mergeTwoLists(list1, list2)
# Output: [1, 1, 2, 3, 4, 4]
#
# Example 2:
# list1 = []
# list2 = []
# mergeTwoLists(list1, list2)
# Output: []
#
# Example 3:
list1 = []
list2 = [0]
mergeTwoLists(list1, list2)
# Output: [0]