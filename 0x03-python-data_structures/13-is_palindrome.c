#include "lists.h"

/**
 * is_palindrome - function that finds out if a linked list is a palindrome
 * @head: pointer to the head of the list
 *
 * Return: 1 if a plaindrome, 0 if not. empty list returns 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast;
	listint_t *prev_slow;
	listint_t *sec_half, *first_half, *rev_sec_half;

	if (!head || !*head)
		return (1);/* Empty list returns 1 */

	slow = head;
	fast = head;
	prev_slow = NULL;
	/* find the middle of the list */
	while (fast && fast->next)
	{
		prev_slow = slow
		slow = slow->next;
		fast = fast->next->next;
	}
	/* Reverse the second half of the list */
	sec_half = NULL;
	if (fast)
	{
		sec_half = slow->next;
	}
	else
	{
		sec_half = slow;
	}
	prev_slow->next = NULL;
	rev_sec_half = reverse_list(sec_half);
	/* Compare first half with reversed second half */
	first_half = *head;
	while (rev_sec_half)
	{
		if (first_half->n != sec_half->n)
			return (0);
		first_half = first_half->next;
		rev_sec_half = rev_sec_half->next;
	}
	return (1);
}

/**
 * reverse_list - function to reverse a list
 * @head: pointer to the head of a node
 *
 * Return: New head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;  /* Store next node */
		current->next = prev;  /* Reverse current node's pointer */
		prev = current;        /* Move prev up */
		current = next;        /* Move to next node */
	}
	return (prev);  /* New head of the reversed list */
}
