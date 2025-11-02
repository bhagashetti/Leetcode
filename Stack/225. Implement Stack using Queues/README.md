Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False


A deque (pronounced “deck”) stands for double-ended queue.
It works like a normal queue (FIFO – First In, First Out), but with extra flexibility: you can add or remove elements from both the front and the back efficiently.

🔑 How it works

Front = the left side of the deque

Back (or rear) = the right side of the deque

Operations you can perform:

append(x) → add element x to the back.

appendleft(x) → add element x to the front.

pop() → remove and return the element from the back.

popleft() → remove and return the element from the front.

All these operations are O(1) (very fast, regardless of the deque size), unlike a normal Python list where inserting/removing from the front can be slo