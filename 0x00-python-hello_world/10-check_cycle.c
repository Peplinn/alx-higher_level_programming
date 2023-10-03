#include "lists.h"

/**
* check_cycle - Checks if a list has a cycle or not
* @list: List head pointer
* Return: 0 if no cycle
* ELSE, 1 cycle.
*/

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
