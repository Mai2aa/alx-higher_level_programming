#include "lists.h"
int check_cycle(listint_t* list)
{
    if (list == NULL || list->next == NULL)
    {
        return (0);
    }
    listint_t *fast, *slow;
    slow = list;
    fast = slow->next;
    while (slow != NULL && fast->next != NULL && fast->next->next != NULL)
    {
        if (slow == fast)
        {
            return (1);
            slow = slow->next;
            fast = fast->next->next;
        }
    }
        return (0);
}

