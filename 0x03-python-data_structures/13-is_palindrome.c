#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * rev_listint -  reverses a listint_t linked list
 * @mid: pointer to first node
 *
 * Return: a pointer to the first node of the reversed list
 */
listint_t *rev_listint(listint_t **mid)
{
	listint_t *prev, *next;

	if ((*mid)->next == NULL)
		return (*mid);
	prev = *mid;
	next = (*mid)->next;
	prev->next = NULL;
	while (next != NULL)
	{
		*mid = next;
		next = next->next;
		(*mid)->next = prev;
		prev = *mid;
	}
	return (*mid);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *end = *head, *ini = *head, *mid = *head;
	int len = 0, i = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (end != NULL)
	{
		end = end->next;
		len++;
	}
	if (len % 2 == 0)
		len++;
	while (i < len / 2)
	{
		mid = mid->next;
		i++;
	}
	rev_listint(&mid);
	while (ini != NULL && mid != NULL)
	{
		if (ini->n != mid->n)
			return (0);
		ini = ini->next;
		mid = mid->next;
	}
	return (1);
}
