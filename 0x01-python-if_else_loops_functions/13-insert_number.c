#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * getValueIndex - Operation to get index to fix new node
 * @head: head of list node
 * @number: value of node
 * Return: int
 */
int getValueIndex(listint_t *head, int number)
{
	int i;

	i = 0;
	while (head->next != NULL)
	{
		if (head->n > number)
			return ((i == 0) ? 0 : (i - 1));
		head = head->next;
		i++;
	}
	return (i);
}

/**
 * insert_node - Operation to insert a number into a sorted linked list
 * @head: pointer to head of list
 * @number: value for tail
 * Return: pointer to tail or null on fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tail, *dup;
	int i, j;

	tail = (listint_t *) malloc(sizeof(listint_t));
	if (tail == NULL)
		return (NULL);
	tail->n = number;

	if (*head == NULL)
	{
		*head = tail;
		return (*head);
	}
	dup = *head;
	i = 0;
	j = getValueIndex(*head, number);
	if (j == 0)
	{
		tail->next = dup;
		return (tail);
	}
	while (dup->next != NULL && i < j)
	{
		dup = dup->next;
		i++;
	}
	tail->next = dup->next;
	dup->next = tail;
	return (tail);
}

