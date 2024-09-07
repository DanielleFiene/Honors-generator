# **Honors Generator & Graduation Countdown**

This project demonstrates the use of Python generators to handle two separate tasks:
1. Awarding academic honors based on GPA.
2. Simulating a countdown to graduation, with the ability to dynamically adjust the countdown.

This code showcases several advanced Python techniques, such as:
- The use of generator functions.
- Control flow using `send()` and `close()` for dynamic interaction with generators.
- Using `yield from` to delegate to sub-generators.

## **Table of Contents**
1. [Learning Goals](#learning-goals)
2. [Code Overview](#code-overview)
3. [Requirements](#requirements)
4. [How to Run the Code](#how-to-run-the-code)
5. [Example Output](#example-output)
6. [Contributing](#contributing)
7. [License](#license)

## **Learning Goals**
The primary learning goals of this project are:
- Understanding **generators** in Python and their use for managing sequences and infinite data streams.
- Learning how to use `yield from` to delegate the behavior of one generator to another.
- Understanding how to control the execution of generators dynamically using `send()` to inject values and `close()` to stop the generator.
- Building real-world examples of asynchronous-like behavior in Python, using generators to manage state and flow in a non-blocking manner.

By completing this project, you will improve your ability to:
- Write and use Python generators for efficient memory handling.
- Implement custom control flow with Python’s generator functions.
- Combine multiple generators to create modular, scalable solutions.

## **Code Overview**

### **1. Academic Honors Generator**
This section of the code awards academic honors based on a list of GPA values:
- **Summa Cum Laude** for GPAs above 3.9
- **Magna Cum Laude** for GPAs between 3.7 and 3.9
- **Cum Laude** for GPAs between 3.5 and 3.7
- **No honors** for GPAs below 3.5

The main generator function, `honors_generator()`, uses the `yield from` statement to delegate to the specific honor-generating functions (`generate_summa_cum_laude()`, `generate_magna_cum_laude()`, and `generate_cum_laude()`).

### **2. Graduation Countdown Generator**
This section simulates a countdown from a given number of days to graduation. The countdown allows for dynamic changes:
- The user can adjust the countdown by sending new values using `send()`.
- The countdown can be stopped early using `close()`.

The `graduation_countdown()` function yields the number of days left and allows for mid-count adjustments.

## **Requirements**
- Python 3.x

No external libraries are required to run this code.

## **How to Run the Code**

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Run the Python file**:
   If you've saved the code in a file called `honors_graduation.py`, run it with:
   ```bash
   python honors_graduation.py
   ```

3. **Observe the Output**:
   The script will first simulate the countdown to graduation, then it will print the honor labels for each GPA in the list.

## **Example Output**

The following is an example of what the output might look like when you run the code:

```text
Days Left: 25
Days Left: 24
Days Left: 23
...
Days Left: 15
Days Left: 10  # Countdown jumps to 10
Days Left: 9
...
Days Left: 4
Days Left: 3  # Countdown stops early

Honor: No honors
Honor: Summa Cum Laude
Honor: Cum Laude
Honor: No honors
```

### **Key Features**
- The countdown adjusts dynamically when certain days are reached (e.g., it jumps to 10 days left when 15 is reached).
- The GPA honor system assigns honors based on academic performance, and non-honored GPAs are handled as well.

## **Contributing**
Contributions are welcome! If you'd like to contribute to this project, feel free to:
- Fork the repository.
- Create a feature branch (`git checkout -b feature-branch-name`).
- Commit your changes (`git commit -m 'Add new feature'`).
- Push to the branch (`git push origin feature-branch-name`).
- Open a Pull Request.

## **License**
This project is licensed under the MIT License. Feel free to use and modify the code.
