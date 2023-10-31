#include "lists.h"
int check_cycle(listint_t* list)
{
    listint_t *fast = list;
    listint_t *slow = list;
    slow = slow->next;
    fast = slow->next->next;
    if (slow == fast)
    {
        return (1);
    }
    else
    {
        return (0);
    }
}

