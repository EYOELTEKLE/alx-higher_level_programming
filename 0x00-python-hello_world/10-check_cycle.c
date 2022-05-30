#include "lists.h"
#include <stdlib.h>
/**
 * check_cycle - checks if a LL has a cycle
 * list: pointer to a list
 * Return: Integer
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow = list;

	if (list == NULL)
		return (0);
	fast = list->next;
	while (fast != NULL && fast->next != NULL)
	{
		if (fast == slow)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
