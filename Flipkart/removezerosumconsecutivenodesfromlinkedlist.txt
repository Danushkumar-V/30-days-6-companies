/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeZeroSumSublists(ListNode head) {
        ListNode dummy = new ListNode(0, head);
        // map with key as prefix sum and value will be the node with that sum
        Map<Integer, ListNode> map = new HashMap<>();
        // put starting value in the map
        map.put(0, dummy);

        int preSum = 0;
        while(head!=null){
            preSum += head.val;
            if(map.containsKey(preSum)){
                // delete all entries of nodes from map, which we want to delete
                ListNode prev = map.get(preSum);
                ListNode node = prev.next;
                
                int sum = preSum;
                while(node != head){
                   sum += node.val;
                   map.remove(sum);
                   node = node.next;
                }
                // delete the nodes
                prev.next = head.next;
            } else {
                map.put(preSum, head);
            }

            head = head.next;
        }

        return dummy.next;
    }
}