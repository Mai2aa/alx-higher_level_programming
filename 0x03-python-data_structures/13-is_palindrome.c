#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if a list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if not a palindrome, 1 if a palindrome
*/
int is_palindrome(listint_t **head)
{
    listint_t *fast = *head, *slow = *head, *prev = NULL,
    *next;

    if (*head == NULL || (*head)->next == NULL) {
        return (1);  // Empty list or list with only one element is considered a palindrome
    }

    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;

        // Reverse the first half of the linked list while traversing
        next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }

    // If the list has an odd number of nodes, move the slow pointer one step further
    if (fast != NULL)
    {
        slow = slow->next;
    }

    // Compare the first half and second half of the linked list
    while (prev != NULL && slow != NULL)
    {
        if (prev->n != slow->n) {
            return (0);  // Not a palindrome
        }
        prev = prev->next;
        slow = slow->next;
    }

    return (1);  // Palindrome
}
