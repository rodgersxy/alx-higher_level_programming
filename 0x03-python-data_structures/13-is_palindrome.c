#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
* is_palindrome - function that checks if a singly linked list
* is a palindrome
* @head: double pointer
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *reverse = NULL;

	/*find the middle node*/
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	/*reverse**/
	reverse = reverse_list(&slow);

	listint_t *current = *head;

	while (current != NULL && reverse != NULL)
	{
		if (current->n != reverse->n)
			return (0);
		current = current->next;
		reverse = reverse->next;
	}
	reverse_list(&slow);

	return (1);
}

/**
* reverse_list -reverse linked list
* @head: double pointer to the head
* Return: pointer to first node of the reverved list
*/

listint_t *reverse_list(listint_t **head)
{
	listint_t *reverse = NULL;
	listint_t *previous = *head;
	listint_t *next = *head;

	while (previous)
	{
		next = next->next;
		previous->next = reverse;
		reverse = previous;
		previous = next;
	}

	return (reverse);
}
