#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - nserts a number into a sorted singly linked list
 * @head: pointer to the head of the list
 * @number: the number to insert
 * Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *node = *head, *new;
    new = malloc(sizeof(listint_t));
    if (new == NULL)
    {
        return NULL;
    }
    new->n = number;
    new->next = NULL;
    if(*head == NULL || number < (*head)->n)
    {
        new->next = *head;
        *head = new;
    }
    else
    {
        while (node->next && number > node->next->n)
        {
            node = node->next;
        }
        new->next = node->next;
        node->next = new;
    }
    return (new);
}
