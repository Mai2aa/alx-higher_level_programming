#include "lists.h"
int check_cycle(listint_t* list)
{
    listint_t *fast = list, *slow = list;
    if (list == NULL || list->next == NULL)
    {
        return (0);
    }
    while (slow && fast && fast->next)
    {
        slow = list->next;
        fast = list->next->next;
        if (slow == fast)
        {
            return (1);
        }
    }
        return (0);
}

