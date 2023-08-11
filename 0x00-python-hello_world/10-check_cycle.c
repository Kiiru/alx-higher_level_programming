#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle - Operation to check if a list has a loop
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	current = list;
	while (current != NULL)
	{
		current = current->next;
		if (current == list)
			return (1);
	}

	return (0);
}

