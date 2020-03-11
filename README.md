# Working with Files and Error Handling Exceptions
Error handling is the important concept of this class.

## Topics
This class will cover:

## Error handling
excptions
using `try` and `except`
best practices using `with`
clean up our functions with `finally`
open, closing and writing to files
Error Handling
What can go wrong will go wrong

Assume your code will break, and what you want to do is handle the errors, gracefully.

When you handle your errors, your code will continue to run.

## Best Practices
**never capture all exceptions**
You never want to handle for **ALL EXCEPTION** because it can create an unstopable code.

You must specify what exception you want to handle:

```python
try:
    file = open('order.txt')
except FileNotFoundError
    print('THERE HAS BEEN AN ERROR! PANIC NOW!')
```

**Capture your message**
You can capture your messages using `as`:

```python
try:
    file = open('order.txt')
except FileNotFoundError as error_message:
    # print('THERE HAS BEEN AN ERROR! PANIC NOW!')
```

## Definitions
###errors and exceptions
It's when the code actually breaks / stops. Unless handled.

**raise**

Key worth ti raise an exception in pythons

**`try:` , `except:` and `finaly:`**
**open() & close()
readline()
readlines()
use with:**
The `with open('file') as file:` implicitly closes the files after it run the block of code.



