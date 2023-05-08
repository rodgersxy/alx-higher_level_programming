#include "lists.h"
/**
 * check_cycle - function that check if the list has cycles or is a loop
 * @list: the list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	/*initialize slow and fast to point to same node as list*/
	slow = fast = list;

	while (slow && fast && fast->next)
	{
		/*moves slow one node forward in the list*/
		slow = slow->next;
		/*moves fast two nodes forward inthe list*/
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}
