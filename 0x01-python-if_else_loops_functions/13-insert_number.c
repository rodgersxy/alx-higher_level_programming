#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

listint_t *create_node(int n);

/**
 * insert_node - inserts a node linked list
 * @head: double pointer to head of list
 * @number: data for new node
 *
 * Return: pointer of new created node, NULL if Fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = NULL, *new_node = NULL;

	if (!head)
		return (NULL);
	else if (!(*head))
	{
		new_node = create_node(number);
		*head = new_node;
		return (new_node);
	}
	current_node = *head;
	while (current_node)
	{
		/* sets current_node to point to  head */
		if (current_node->n >= number)
		{
			new_node = create_node(number);
			new_node->next = current_node;
			*head = new_node;
			return (new_node);
		}
		else if (current_node->n <= number)
		{
			/*check value of current to insert*/
			if (!current_node->next || current_node->next->n >= number)
			{
				/*new node is returned*/
				new_node = create_node(number);
				new_node->next = current_node->next;
				current_node->next = new_node;
				return (current_node->next);
			}
		}
		current_node = current_node->next;
	}

	/*failed to insert*/
	return (NULL);
}


/**
 * create_node - function to create new node in the linked list
 * @n: data to insert into new node
 *
 * Return: pointer to the new  node
 */
listint_t *create_node(int n)
{
	/* Allocate memory for the new node */
	listint_t *new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);

	/* Initialize the node's data */
	new_node->n = n;
	new_node->next = NULL;

	return (new_node);
}
