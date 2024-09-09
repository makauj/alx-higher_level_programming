#include "lists.h"

/**
 * check_cycle - function that checks for a cycle in a linked list
 * @list: singly-linked list
 *
 * Return: 1 if there is a cycle, else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (!list || list->next == NULL)
	{
		return (0);
	}
	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
