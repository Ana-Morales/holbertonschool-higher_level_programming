#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *ini = *head, *end = *head;
	int len = 0, i = 0, j;

	if (*head == NULL)
		return (1);
	while (end->next != NULL)
	{
		end = end->next;
		len++;
	}
	while (i <= len / 2)
	{
		if (ini->n != end->n)
			return (0);
		ini = ini->next;
		end = *head;
		j = 0;
		while (j < (len - i - 1))
		{
			end = end->next;
			j++;
		}
		i++;
	}
	return (1);
}
