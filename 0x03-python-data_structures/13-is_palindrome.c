#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - checks if a list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if not a palindrome, 1 if a palindrome
*/
int is_palindrome(listint_t **head)
{
    listint_t *fast = *head, *slow = *head, *prev = *head,
    *next, *mid = NULL;
    int result = 1;
    if (*head == NULL || (*head)->next == NULL)
        return (1);
    while (fast && fast->next)
        {
            fast = fast->next->next;
            next = slow->next;
            slow->next = prev;
            prev = slow;
            slow = next;
        }
    if (fast != NULL)
        {
            mid = slow;
            slow = slow->next;
        }
    while (slow != NULL)
        {
            if (prev->n != slow->n)
            {
                result = 0;
                break;
            }
            prev = prev->next;
            slow = slow->next;
        }
    while (prev != NULL)
    {
        next = prev->next;
        prev->next = slow;
        slow = prev;
        prev = next;
    }
    if (mid != NULL)
        mid->next = slow;
    return (result);
    }
