#include list.h

/**
  * check_cycle - checks if a linked list contains a cycle.
  * @list: list to check
  *
  * Return: 1 if the list has a cycle, otherwise 0.
  */
int check_cycle(listint_t *list)
{
	listint_t *start = list;
	listint_t *end = list;

	if (!list)
		return (0);
	while (start && end && end->next)
	{
		start = start->next;
		end = end->next->next;
		if (start == end)
			return (1);
	}
	return (0);
}
