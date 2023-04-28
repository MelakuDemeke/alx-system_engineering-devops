#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - a function that runs forever and returns nothing
 * @void: no parameters
 *
 * This function runs an infinite loop that sleeps for 1 second
 */
void infinite_while(void)
{
	while (1)
		sleep(1);
}

/**
 * main - the entry to a program that creates 5 zombie processes
 * @void: no parameters
 *
 * This program creates 5 child processes using fork() and prints their PIDs,
 * but doesn't wait for them to terminate, so they become zombie processes.
 * Then, it enters an infinite loop, waiting for signals or other events.
 *
 * Return: 0 on success
 */
int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		pid_t pid = fork();

		if (pid == -1)
		{
			perror("fork");
			exit(1);
		}
		if (pid == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", pid);
	}

	infinite_while();

	return (0);
}
