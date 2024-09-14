# Check if linked list is a palindrome
## The question:
Write a function in C that checks if a singly linked list is a palindrome.

- Prototype: int is_palindrome(listint_t **head);
- Return: 0 if it is not a palindrome, 1 if it is a palindrome
- An empty list is considered a palindrome

## Whiteboarding
### 1. Problem understanding
A palindrome is a word or phrase that reads the same backwards as forwards.
For this problem, the list would have to read the same backwards as forwards.
For example, 1->2->3->3->2->1 is a palindrome.

### 2. Approach.
1. iterate through the list using a slow pointer and a fast pointer to find the middle of the list
2. reverse the second half of the list and iterate through it
3. compare the two halves to determine if they are identical.
4. restore the list to its original form

### Detailed Steps
1. Find the middle:
	- Initialize two pointers, fast and slow, to the head of the list
	- The slow pointer moves one step at a time `slow = slow->next`
	- The fast pointer moves two steps at a time `fast = fast->next->next
	- When the fast pointer reaches the end of the list, the slow one will be in the middle of the list.
2. Reverse the second half:
	- After finding the middle, reverse the second half starting from `slow->next`
3. Comparing Both Halves:
	- Compare the nodes of the first half of the list with the nodes of the reversed second half.
4. Restoring the List:
	- To preserve the original list, reverse the second half back to its original form after the comparison.

##Pseudocode

```pseudocode
FUNCTION is_palindrome(head)
    IF head IS NULL OR head.next IS NULL
        RETURN 1  /* An empty list is a palindrome */

    /* Step 1: Find the middle of the list */
    SET slow TO head
    SET fast TO head
    SET prev_of_slow TO NULL

    WHILE fast IS NOT NULL AND fast.next IS NOT NULL
        SET fast TO fast.next.next
        SET prev_of_slow TO slow
        SET slow TO slow.next

    /* Step 2: Reverse the second half of the list */
    SET second_half TO slow
    SET prev_of_slow.next TO NULL  /* Split the list into two halves */
    SET second_half TO reverse_list(second_half)

    /* Step 3: Compare the two halves */
    SET first_half TO head
    WHILE second_half IS NOT NULL
        IF first_half.n IS NOT equal TO second_half.n
            RETURN 0  /* Not a palindrome */
        SET first_half TO first_half.next
        SET second_half TO second_half.next

    RETURN 1  /* Is a palindrome */
END FUNCTION
```
