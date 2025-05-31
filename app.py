class Counter:
    """
    A class that keeps track of the number of objects created from it.
    """
    _count = 0  # Class variable to store the count of objects

    def __init__(self):
        """
        Constructor to increment the object count when a new object is created.
        """
        Counter._count += 1

    @classmethod
    def get_object_count(cls):
        """
        Class method to retrieve the current number of objects created.

        Args:
            cls: Refers to the class itself (Counter in this case).

        Returns:
            int: The total number of objects created from the Counter class.
        """
        return cls._count

# Create several instances of the Counter class
c1 = Counter()
c2 = Counter()
c3 = Counter()

# Display the object count using the class method
print(f"Number of Counter objects created: {Counter.get_object_count()}")

c4 = Counter()
print(f"Number of Counter objects created: {Counter.get_object_count()}")