#include "lists.h"


/**
 * length_of_list - Operation to find the length of a list
 * @s: pointer to pointer to list
 * Return: int length of a linked list
 */
int length_of_list(listint_t **s)
{
	int i;

	i = 0;
	while ((*s)->next != NULL)
	{
		i++;
		*s = (*s)->next;
	}

	return (i);
}

/**
 * _print_rev_recursion - operation to return a string in reverse
 * @s: pointer to string array
 * @c: reversed string
 * Return: reversed string
 *
*/
void _print_rev_recursion(listint_t *s, char* c)
{
	printf("_print_rev_recursion called!");
	if (s->next == NULL)
		return;
	else
	{
		c += s->n + '0';
		_print_rev_recursion(s->next, c);
	}
}

/**
 * _print_forward - Operation to return a char array of a linked list
 * @s: Linked list
 * Return: char array
 *
 */
char * _print_forward(listint_t **s)
{
	char *c;
	c = malloc(sizeof(char) * length_of_list(s));
	if (c == NULL)
		exit(1);
	while ((*s)->next != NULL)
	{
		c = (*s)->n + '0';
		*s = (*s)->next;
		c++;
	}

	return (c);
}

/**
 * is_palindrome - Operation to check if a list is a palindrome
 * @head: linked list
 * Return: 0 if head is not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	char* forward;
	char* backward;

	printf("checking if head is null or empty\n");
	if (head == NULL || (*head)->next == NULL)
		return (1);

	printf("Allocating memory to the string pointer\n");
	forward = malloc(sizeof(char) * length_of_list(head));
	backward = malloc(sizeof(char) * length_of_list(head));

	printf("Checking if memory allocation was successful\n");
	if (forward == NULL || backward == NULL)
		return (0);

	printf("Getting the reverse string!\n");
	_print_rev_recursion(*head, backward);
	printf("%s\n",backward);
	printf("Getting the forward string!\n");
	forward = _print_forward(head);
	printf("%s\n", forward);

	if (forward == backward)
		return (1);
	else
		return (0);
}
