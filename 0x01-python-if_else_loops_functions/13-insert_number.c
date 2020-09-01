#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head: pointer to head of list
 * @number: number to be inserted
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *temp;

	current = *head;
	temp = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (current != NULL && current->n < number)
	{
		temp = current;
		current = current->next;
	}
	new->next = current;
	temp->next = new;
	return (new);
}
