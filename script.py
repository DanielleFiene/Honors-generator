# Honor Label Generators
def generate_summa_cum_laude():
    """Yields 'Summa Cum Laude' label for GPAs above 3.9."""
    yield 'Summa Cum Laude'

def generate_magna_cum_laude():
    """Yields 'Magna Cum Laude' label for GPAs between 3.7 and 3.9."""
    yield 'Magna Cum Laude'

def generate_cum_laude():
    """Yields 'Cum Laude' label for GPAs between 3.5 and 3.7."""
    yield 'Cum Laude'

# Honors Generator based on GPA
def honors_generator(gpas):
    """
    Takes a list of GPAs and yields the appropriate honors.
    - If GPA > 3.9: Summa Cum Laude
    - If GPA > 3.7: Magna Cum Laude
    - If GPA > 3.5: Cum Laude
    - Otherwise, no honors are awarded.
    """
    for gpa in gpas:
        if gpa > 3.9:
            # Yield from the 'Summa Cum Laude' generator if GPA > 3.9
            yield from generate_summa_cum_laude()
        elif gpa > 3.7:
            # Yield from the 'Magna Cum Laude' generator if GPA > 3.7
            yield from generate_magna_cum_laude()
        elif gpa > 3.5:
            # Yield from the 'Cum Laude' generator if GPA > 3.5
            yield from generate_cum_laude()
        else:
            # Yield "No honors" if GPA does not meet any threshold
            yield "No honors"

# Graduation Countdown Generator
def graduation_countdown(days):
    """
    Countdown generator that starts from a given number of days until graduation.
    - Yields the current number of days left.
    - Allows external input to adjust the countdown (using `send()`).
    - Stops early if `close()` is called.
    """
    while days >= 0:
        # Yield the current number of days left in the countdown
        days_left = yield days
        if days_left is not None:
            # If a new number of days is sent in (via `send()`), adjust the countdown
            days = days_left
        else:
            # Otherwise, decrement the countdown by 1
            days -= 1

# Function to test the graduation countdown generator
def test_graduation_countdown(days):
    """
    Simulates the graduation countdown, with mid-count adjustments.
    - If the countdown reaches 15 days, jump ahead to 10 days.
    - If the countdown reaches 3 days, the countdown is stopped early.
    """
    countdown = graduation_countdown(days)
    for day in countdown:
        if day == 15:
            # On day 15, send 10 to reset the countdown to 10 days left
            countdown.send(10)
        elif day == 3:
            # On day 3, close the generator and stop the countdown early
            countdown.close()
        # Print the current number of days left
        print(f"Days Left: {day}")

# Function to test the honors generator
def test_honors_generator():
    """
    Test the honors_generator function with a sample list of GPAs.
    For each GPA, the function yields the appropriate honors.
    """
    gpas = [3.2, 4.0, 3.6, 2.9]  # Sample list of GPAs
    honors = honors_generator(gpas)
    for honor in honors:
        # Print the honor label for each GPA in the list
        print(f"Honor: {honor}")

# Run the countdown simulation with 25 days until graduation
days = 25
test_graduation_countdown(days)

# Test the honors generation with sample GPA values
test_honors_generator()
