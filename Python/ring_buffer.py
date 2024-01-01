#!/usr/bin/env python3

from termcolor import colored

class RingBuffer:
    """
    A class representing a ring buffer data structure.

    Attributes
    ----------
    head : int
        The index of the head element in the buffer.
    tail : int
        The index of the next insertion point in the buffer.
    size : int
        The current number of elements in the buffer.
    capacity : int
        The maximum capacity of the buffer.
    buffer : list
        The list representing the buffer contents.

    Methods
    -------
    enBuffer(value: int)
        Adds a value to the end of the buffer, removing the oldest element if the buffer is full.
    deBuffer()
        Removes the oldest element from the buffer.
    front() -> int
        Returns the value at the front of the buffer.
    rear() -> int
        Returns the value at the rear of the buffer.
    isEmpty() -> bool
        Checks if the buffer is empty.
    isFull() -> bool
        Checks if the buffer is full.
    display()
        Displays the current state of the buffer.

    """

    def __init__(self, capacity: int):
        """
        Constructs all the necessary attributes for the RingBuffer object.

        Parameters
        ----------
        capacity : int
            The maximum number of items the buffer can hold.

        """
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = capacity
        self.buffer = [None]*capacity


    def enBuffer(self, value: int) -> None:
        """
        Adds a value to the end of the buffer.

        If the buffer is full, it removes the oldest element before adding the new one.

        Parameters
        ----------
        value : int
            The value to be added to the buffer.

        """
        if self.isFull():
            self.deBuffer()
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size = min(self.size + 1, self.capacity)
        return True

    def deBuffer(self) -> None:
        """
        Removes the oldest element from the buffer.

        Raises
        ------
        ValueError
            If the buffer is empty.

        """
        if self.isEmpty(): 
            raise ValueError("Cannot dequeue from an empty buffer")
        self.head = (self.head+1)%self.capacity
        self.size -= 1
        return True

    def front(self) -> int:
        """
        Returns the value at the front of the buffer.

        Raises
        ------
        ValueError
            If the buffer is empty.

        Returns
        -------
        int
            The value at the front of the buffer.

        """
        if self.isEmpty(): 
            ValueError("Cannot get front of an empty buffer")
        return self.buffer[self.head]

    def rear(self) -> int:
        """
        Returns the value at the rear of the buffer.

        Raises
        ------
        ValueError
            If the buffer is full.

        Returns
        -------
        int
            The value at the rear of the buffer.

        """
        if self.isFull(): 
            raise ValueError("Cannot get rear of a full buffer")
        return self.buffer[self.tail-1]

    def isEmpty(self) -> bool:
        """ Checks if the buffer is empty. """
        return self.size == 0

    def isFull(self) -> bool:
        """ Checks if the buffer is full. """
        return self.size == self.capacity
    
    def display(self):
        """ Display the current state of the buffer. """
        buffer_visual = [colored("[ ]", "white") for _ in range(self.capacity)]
        idx = self.head
        for _ in range(self.size):
            buffer_visual[idx] = colored(f"[{self.buffer[idx]}]", "green")
            idx = (idx + 1) % self.capacity
        print("Buffer State: " + ' '.join(buffer_visual))
    
if __name__ == "__main__":
    try:
        capacity = int(input("Enter the capacity of the buffer: "))
        buffer = RingBuffer(capacity)

        while True:
            print("\nOptions:")
            print("1. Enqueue value")
            print("2. Dequeue value")
            print("3. Display buffer state")
            print("4. Exit")

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == "1":
                value = int(input("Enter the value to enqueue: "))
                buffer.enBuffer(value)
                print(f"Enqueued value {colored(value, 'cyan')}")
                buffer.display()

            elif choice == "2":
                if buffer.deBuffer():
                    print(f"Dequeued value {colored('success', 'green')}")
                else:
                    print(colored("Buffer is empty. Cannot dequeue.", "red"))
                buffer.display()

            elif choice == "3":
                buffer.display()

            elif choice == "4":
                print(colored("Exiting program.", "yellow"))
                break

            else:
                print(colored("Invalid choice. Please enter a valid option.", "red"))

    except ValueError as e:
        print(colored(f"Error: {e}", "red"))
    except KeyboardInterrupt:
        print(colored("\nExiting program.", "yellow"))
    except Exception as e:
        print(colored(f"Unexpected error: {e}", "red"))