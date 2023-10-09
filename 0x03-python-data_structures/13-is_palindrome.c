#include "lists.h"

/**
* is_palindrome - Checks if singly linked list is palindrome
* @head: List head
* Return: 0 if not palindrome, ELSE 1 if palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *head2;
	int palindrome = 1;

	/* Find list center */
	slow = fast = *head;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast == NULL)
		head2 = slow;
	else
		head2 = slow->next;

	/* Reverse second half*/
	slow = NULL;
	while (head2 != NULL)
	{
		fast = head2->next;
		head2->next = slow;
		slow = head2;
		head2 = fast;
	}
	head2 = slow;

	/* Compare first and second */
	slow = *head;
	fast = head2;
	while (slow && fast)
	{
		if (slow->n != fast->n)
		{
			palindrome = 0;
			break;
		}
		slow = slow->next;
		fast = fast->next;
	}

	/* Reverse second, link to first */
	slow = NULL;
	while (head2 != NULL)
	{
		fast = head2->next;
		head2->next = slow;
		slow = head2;
		head2 = fast;
	}
	head2 = slow;

	/* Return the result */
	if (palindrome)
		return (1);
	return (0);
}
