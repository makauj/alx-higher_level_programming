#include "lists.h"

/**
 * insert_node - function that inserts a number in a linked list
 * @head: head of a node
 * @number: number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current, *previous;

	if (!head)
	{
		return (NULL);
	}
	new = malloc(sizeof(listint_t));
	if (!new)
	{
		return (NULL);
	}

	current = *head;
	new->n = number;
	previous = NULL;

	while (current != NULL && current->n < number)
	{
		previous = current;
		current = current->next;
	}
	previous->next = new;
	new->next = current;

	return (head);
}
