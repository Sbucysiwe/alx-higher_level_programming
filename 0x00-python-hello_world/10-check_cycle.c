#include "lists.h"
/**
*has_cycle -detects cycles in linked lists.
*@linked_list: The linked list being examined.
* Return: 1 if the list has a cycle, 0 if it doesn't
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
