#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * check_cycle - checks if a list has a cycle
 * @list: pointer to list
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t* list)
{
    listint_t *fast = list;
    listint_t *slow = list;
    while (fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast)
        {
            return (1);
        } 
    }
    return (0);
}
