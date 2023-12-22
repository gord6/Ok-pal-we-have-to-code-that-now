
## Task 1: Array Manipulation
Implement the Class ArrayManipulator that is passed an array (or in Python a list) of integers as attributes and implements the following methods:

**Java** / **Python**

1. **reverseArray** / **reverse_list**: This method reverses the array so that the first element becomes the last. The second last and so on. 
After that, the reversed array is to be returned. 

2. **sortDescending/sort_descending**: This method sorts the array in descending order and then returns the first element of the sorted array.

3. **findDuplicate** / **find_duplicate**: This method searches for a duplicate in the array and returns it. It is guaranteed that there is exactly one duplicate in the array.

4. **doubleOddNumbers** / **double_odd_numbers**: This method doubles each odd value in the array and returns the array. 

5. **removeElement** / **remove_element**: This method takes an int *element*. The method checks if the element exists in the array. If it is present, it is deleted and the method returns the boolean value *true*. Otherwise, the method returns *false*. 




## Task 2: Bank 

**Task 2: Bank**
Given the program code from the files "Person.java", "Account.java" or "Person.py" and "Account.py", where classes are already implemented. Your task is to model and implement a class for a bank which takes on the following responsibilities:
Constructor: Creates a database in which any number of accounts can be stored.

1. **addAccount/add_account**: Adds a new account to the database. For this, the information needed to create an account is provided. This method should return the number of accounts.

2. **transferAccount/transfer_account**: Changes the owner of an account. For this, two people are provided: the current account holder and the new account holder. The operation is also password protected: a password is provided, which must match the password of the current account holder for the operation to be carried out. Assume that each person can only have one account. This method should return a boolean value.

3. **deleteAccount/delete_account**: Removes the account of the provided person. This operation is password protected. This method should return a boolean value.

4. **getAllAccounts/get_all_accounts**: Returns all accounts in an array.

5. **withdraw**: Withdraws the given sum from the account of the given holder. This operation is password protected. This method should return a boolean value.

6. **deposit**: Deposits the given sum into the account of the given person. This operation is password protected. This method should return a boolean value.




## Task 3: Double Linked List
In the file "DoubleLinkedList.java" or "DoubleLinkedList.py", you will find the beginning of an implementation for a double linked list. Implement the following functions for the class:

1. **append**: Adds an integer value to the end of the list.

2. **get**: Receives an index and returns the element at that position. If the index is not in the list, return null (or None in Python).

3. **length**: Returns the length of the list.

4. **insert**: Receives a position and an integer value and adds the integer value at the given position.

5. **toString (Java) / __str__ (Python)**: Converts the contents of the list into a string in the internal order and formats it in a readable manner. For example, elements can be connected by a <-> (e.g., 1<->2<->3<->4<->5).

6. **contains**: Receives an integer value and should return an array of index values at which this number can be found.





## Task 4: Queue
Implement a queue that uses a list of your choice as its internal storage and stores integers. You should not implement your own list from scratch.

1. **offer**: Adds an element to the end of the queue.

2. **poll**: Removes an element from the beginning of the queue and returns the removed element.

3. **peek**: Returns the element at the beginning of the queue without removing it from the queue.

4. **isEmpty**: Checks whether the queue is empty.

5. **invert**: Takes any queue as input and inverts it using no more than one other queue. Return the inverted queue. The input queue can be modified in this process.





## Task 5.1 

Implement an interface **Geometric**, which provides the following methods:

**geometricDescription()**, which should return a description of how the object could be drawn.

Furthermore, the interface **ZeroDimensional** is to be implemented, which extends the interface Geometric with the following methods:

**getDistance(ZeroDimensional)**, which calculates the Euclidean distance to the given object. <br>
**getX()**, which returns the X-coordiate. <br>
**getY()**, which returns the Y-coordinate. <br>
**geometricDescription()**, which returns the coordinates of the object.

In addition, the interface **OneDimensional** is to be implemented, which extends the interface **Geometric** with the following methods:

**getLength()**, which returns the length of the object.<br>
**geometricDescription()**, which returns the coordinates of the start and end point.

The last interface to be implemented is **TwoDimensional**, which is to extend **Geometric** with the following methods
the following methods:

**getCircumference()**, which shall return the circumference of the object.<br>
**geometricDescription()**, which returns a list of points so that the shape is created from the lines drawn between consecutive points.
Implement a class for each interface.

### Task 5.2
Implement a superclass *Animal*. The class *Animal* shall implement the following methods:

**makeSound()**, which returns a string corresponding to the sound. <br> 
**getNumberOfLegs()**, which returns the number of legs.<br>
**getWeight()**, which returns the effective weight of the animal.<br>

Implement the following animals as derived classes of Animal with the appropriate methods:

*Dog* <br>
**isBarking()**, which sets the sound of the dog to a bark. <br>
**isHowling()**, which sets the sound of the dog to a howl.

*Donkey* <br>
***pack(int)***, which loads the donkey with additional weight, increasing its effective weight. <br>
**unpack(int)**, which takes extra weight off the donkey and thus decreases its effective weight.

### Task 5.3
Consider when to use an interface and when to use inheritance?

### Task 5.4 

Write a class that implements mathematical operations **generically**. Do not use methods from the *Math* class. The following methods are to be implemented:

**max`<T>`(T valueOne, T valueTwo)**, which returns the maximum value. <br>
**min`<T>`(T valueOne, T valueTwo)**, which returns the minimum value.<br>
**abs`<T>`(T value)**, which returns the absolute value.<br>
**sign`<T>`(T value)**, which returns -1 if the number is less than 0, otherwise 1.

Bonus:<br>
Find a way that only numeric values are used for the **generics**.



## Task 6

You are given the task of revising the code of the "Character" class. You have the following information about what the code should be able to do:
You want to simulate an adventurer from a game who can fight various monsters.
The adventurer has a total of 5 possible actions:
    - Fight an undead
    - Fight a giant spider
    - Fight a dragon
    - Fight a demon
    - Rest
An adventurer always starts his journey with 10 health points, 10 magic points, level 0 and 0 experience points. He or she also has no skills that are of any use to him or her on the adventure.
The adventurer must be assigned a name at creation.
By defeating an undead, basic skills in the use of healing and attacking spells are learned.
Defeating a giant spider teaches basic sword and bow skills and bow.
A dragon is a particularly strong monster. For fighting a dragon you will need
basic skills in handling the sword and the bow.
If the dragon can be slain, the adventurer masters the skills in handling the sword and the bow completely.
A demon is a particularly strong monster. For the fight against a demon basic skills in the use of attack and healing spells are needed.
If the demon can be fought, the adventurer has fully mastered the skills in the use of spells.
Each battle gives 200 experience points. When 200 experience points or a multiple of it are reached, the adventurer advances one level.
Adventurers can rest to heal wounds. If a character has suffered particularly severe wounds, it takes a long time for magic and health points to heal. If he has less than five magic points, each day the amount of two points divided by the character's life points are healed. If the character has five or more life points, two magic points regenerate each every day.
If he has less than five health points, one health point heals each day. If he has five or more
Health points, four Health points regenerate per day.


You will find that the code you are supposed to work with contains many errors and problems. So your task is mainly to improve it through debugging and refactoring. To do this, perform the following steps:


- Correct the syntax errors in the code so that you can execute it.
- Write a main method to test the code. Consider the following tips:
    - Create at least one object of the class
    - Output the attributes of the object to be checked
    - A toString method that makes sense of the object can be helpful
    - Class- Check the state of the object whenever you manipulate it with a method
    - Manipulate the object with all possible methods. Think of different scenarios that can occur.
- To test individual methods, as opposed to complete scenarios, unit tests can be useful. To use unit tests, proceed as follows:
    - Find out how to use unit tests in your language and IDE.
    - Write a simple test that creates an object of your class and check the attributes using assert methods.
    - Write a unit test for each method
    - Note: An additional constructor that allows you to simulate the class in different states can be helpful.
    - Identify edge cases and cover them with additional unit tets

- If you find errors using your tests, the next step is to find and fix them:
    - Find out how the debugger works in your IDE.
    - Set a breakpoint at the point where a unit test failed or where an output does not meet expectations.
    - Find the error using the step-into and step-over functions.
- To increase the readability of the code, refactor it. To do this, use the tools provided by your IDE. The following points can improve readability:
    - Replace ambiguous and incoherent identifier names with ones that conform to your language's conventions and are coherent within the class.
    - Reduce the length and complexity of methods by offloading individual functionalities into their own methods (a good rule of thumb is that a method should have exactly one task).
    - Remove code duplication by offloading functionalities that are needed multiple times into their own methods.

**For advanced students**:
- To make code easier to extend and thus more durable, you can improve code modularization. For example, outsource the monsters to their own classes.
- You can handle some common error sources with the help of exceptions, such as the possibility of a division by 0 in the rest method. Find out about exception handling in your language.

## Task 7

Implement or complete the code from the lecture:
Create a class *BinaryTreeNode* that has the attributes *value*, *left* for the left child and *right* for the right child. Implement constructors, getters, and setters as necessary.
Create a class *BinaryTree*, which has as attribute a *BinaryTreeNode* named *root*. Again, implement constructors, getters, and setters as necessary.
Also implement the following traversal methods to output the values of the tree:
- inorder
- preorder - postorder - level order

**Part 1: Extending the basic methods**
Implement the following methods for your binary tree:
- *contains* - which is passed a value. It returns 'true' if the value is present in the tree, or 'false' if the value is not present.
- *toListInorder* - which stores the values of the tree in a list and returns it.

**Part 2: Advanced methods**
Implement the following methods for your binary tree:
- *insert* - which inserts a node with the given value into the first free space in the tree, if the value does not already exist in the tree.
- *getHeight* - which returns the height of a tree. The height of the tree is equal to the number of levels the tree has. An empty tree has the height 0.
- *delete* - which deletes the node with the given value from the tree by replacing the value with the value of the 'deepest' node in the tree and then deleting that node. The deepest node is the node furthest down and furthest to the right.

## Bonus: Ternary tree
Implement a ternary tree structure, that is, a tree structure where each element has three children: A left child, a middle child, and a right child. Implement the four traversal methods, as well as an insert and a delete method.