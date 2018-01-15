/* You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807. */

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode first = l1;
        ListNode second = l2;
        ListNode results = null;
        ListNode curr = results;
        boolean firstIteration = true;
        int extra = 0;
        
        while (first != null && second != null) {
            int sum = first.val + second.val;
            System.out.println("Sum = " + sum);
            
            if (sum >= 10) {
                sum -= 10;
                extra = 1;
            }
            
            if (curr == null) {
                curr = new ListNode(sum);
                results = curr;
            } else {
                curr.next = new ListNode(sum);
                curr = curr.next;
            }
            
            first = first.next;
            second = second.next;
            
            if (extra > 0) {
                if (first != null) {
                    ListNode temp = first.next;
                    first = new ListNode(first.val + extra);
                    first.next = temp;
                } else if (second != null) {
                    ListNode temp = second.next;
                    second = new ListNode(second.val + extra);
                    second.next = temp;
                } else {
                    curr.next = new ListNode(extra);
                    curr = curr.next;
                }
                extra = 0;
            }
        }
        
        // finish if the lists were not the same size
        System.out.println("The lists weren't the same size. First is done? " + (first == null) + ". Second is done? " + (second == null));
        ListNode onlyList = null;
        
        if (first == null) {
            onlyList = second;
        } else {
            onlyList = first;
        }
        
        while (onlyList != null) {
            int sum = onlyList.val + extra;
            System.out.println("Sum = " + sum);
            
            if (sum >= 10) {
                extra = 1;
                sum -= 10;
            } else {
                extra = 0;
            }
            
            curr.next = new ListNode(sum);
            curr = curr.next;
            onlyList = onlyList.next;
            
            if (onlyList == null && extra > 0) {
                curr.next = new ListNode(extra);
            }
        }
        
        return results;
    }
}