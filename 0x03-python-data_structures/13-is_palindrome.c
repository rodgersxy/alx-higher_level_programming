#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
* is_palindrome - the function that checks if a singly
* linked list is a palindrome.
* @head: double pointer to the list head
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
	int node = 0, i = 0, *array = NULL;

	listint_t *temp = *head;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);
	while (temp)
	{
		node++;
		temp = temp->next;
	}
	/*allocating memory*/
	array = malloc(sizeof(int) * node);
	temp = *head;
	while (temp)
	{
		array[i++] = temp->n;
		temp = temp->next;
	}

	for (i = 0; i < node / 2; i++)
	{
		if (array[i] != array[node - 1 - i])
		{
			free(array);
			return (0);
		}
	}

	free(array);
	return (1);
}
