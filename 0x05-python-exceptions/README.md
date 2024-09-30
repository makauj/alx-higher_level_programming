# 0x05-python-exceptions

## Learnig Objectives

#### 1. What’s the difference between errors and exceptions
**Errors** are prpblems that cause a program to stop it execution.
**Exceptios** are raised when an internal event changes the program's normal flow.
| Type |Errors|Exceptions|
| ___ | ___ | ___ |
|Nature of the issue|These are serious issues that typically arise from the environment in which the application is running. They are often beyond the control of the application and usually indicate problems that cannot be recovered from, such as running out of memory or a system crash. | These are issues that arise within the application itself and can often be anticipated and handled. They represent conditions that a program might want to catch and handle to maintain normal flow.|
| Handling | Generally, errors are not meant to be caught or handled by the application. They are considered fatal and usually result in the termination of the program. |  Exceptions can be caught and handled using try-catch blocks. This allows the program to recover from the exception and continue executing.|
| Recoverability |These are generally not recoverable. Once an error occurs, the best course of action is usually to log the error and exit the program. | These are often recoverable. By catching and handling exceptions, a program can provide more informative error messages and prevent crashes.|
| Examples | Examples include: OutOfMemoryError, StackOverflowError, and VirtualMachineError. | Examples include: NullPointerException, IOException, and IllegalArgumentException. |
#### 2. What are exceptions and how to use them
Exceptions are conditions that arise in a program during execution. They signal that something unexpected has happened.
Exceptions are represented as objects of a specific type in Python, the **Exception class**. They even have descriptive names eg ZeroDivisionError exception, a subclass of the Exception Class.
```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- Exception
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      .....
```
#### 3. When do we need to use exceptions
Exceptions are used to handle unexpected or exceptional conditions that disrupt the normal flow of a program. Here are some key scenarios where you might need to use exceptions:

1. **Error Handling**: When an error occurs that you cannot handle locally, such as a file not being found, a network connection failing, or invalid user input¹.
2. **Separating Error-Handling Code from Regular Code**: Exceptions help keep your main code clean and readable by separating the error-handling logic¹.
3. **Propagating Errors**: When you need to pass an error up the call stack to be handled at a higher level in the program².
4. **Resource Management**: Ensuring that resources like files or network connections are properly closed or released, even if an error occurs².
5. **Unexpected Conditions**: Handling conditions that are not expected to occur during normal operation, such as accessing an external API and encountering a failure³.

In summary, exceptions should be used sparingly and only in situations where they provide a clear benefit in managing errors and maintaining code clarity.

¹: [Oracle Java Tutorials](https://docs.oracle.com/javase/tutorial/essential/exceptions/advantages.html)
²: [Baeldung on Exception Handling](https://www.baeldung.com/java-exceptions)
³: [Culttt on Using Exceptions](https://culttt.com/2014/04/09/use-exception/)

#### 4. How to correctly handle an exception
#### 5. What’s the purpose of catching exceptions
#### 6. How to raise a builtin exception
#### 7.. When do we need to implement a clean-up action after an exception
