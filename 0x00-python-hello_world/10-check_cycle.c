#include "lists.h"
int check_cycle(listint_t* list)
{
    listint_t *fast = list->next, *slow = list;
    if (list == NULL || list->next == NULL)
    {
        return (0);
    }
    while (slow && fast && fast->next)
    {
        if (slow == fast)
        {
            return (1);
        }
        slow = list->next;
        fast = list->next->next;
    }
        return (0);
}

