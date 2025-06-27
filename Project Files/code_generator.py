def generate_code(task_description: str):
    """
    Generate Python code based on keywords in the task description.
    Extend this function or integrate with an AI API for advanced code generation.
    """
    desc = task_description.lower()
    if "addition" in desc:
        return "def add(a, b):\n    return a + b"
    elif "multiplication" in desc:
        return "def multiply(a, b):\n    return a * b"
    elif "swapping" in desc:
        return "def swap(a, b):\n    a, b = b, a\n    return a, b"
    elif "factorial" in desc:
        return (
            "def factorial(n):\n"
            "    if n == 0:\n"
            "        return 1\n"
            "    else:\n"
            "        return n * factorial(n-1)"
        )
    elif "palindrome" in desc:
        return (
            "def is_palindrome(s):\n"
            "    return s == s[::-1]"
        )
    elif "fibonacci" in desc:
        return (
            "def fibonacci(n):\n"
            "    a, b = 0, 1\n"
            "    for _ in range(n):\n"
            "        a, b = b, a + b\n"
            "    return a"
        )
    elif "prime" in desc:
        return (
            "def is_prime(n):\n"
            "    if n <= 1:\n"
            "        return False\n"
            "    for i in range(2, int(n ** 0.5) + 1):\n"
            "        if n % i == 0:\n"
            "            return False\n"
            "    return True"
        )
    elif "reverse" in desc:
        return (
            "def reverse_list(lst):\n"
            "    return lst[::-1]"
        )
    elif "sort" in desc:
        return (
            "def sort_list(lst):\n"
            "    return sorted(lst)"
        )
    elif "gcd" in desc or "greatest common divisor" in desc:
        return (
            "def gcd(a, b):\n"
            "    while b:\n"
            "        a, b = b, a % b\n"
            "    return a"
        )
    elif "lcm" in desc or "least common multiple" in desc:
        return (
            "def lcm(a, b):\n"
            "    def gcd(x, y):\n"
            "        while y:\n"
            "            x, y = y, x % y\n"
            "        return x\n"
            "    return abs(a * b) // gcd(a, b)"
        )
    elif "binary search" in desc:
        return (
            "def binary_search(arr, target):\n"
            "    left, right = 0, len(arr) - 1\n"
            "    while left <= right:\n"
            "        mid = (left + right) // 2\n"
            "        if arr[mid] == target:\n"
            "            return mid\n"
            "        elif arr[mid] < target:\n"
            "            left = mid + 1\n"
            "        else:\n"
            "            right = mid - 1\n"
            "    return -1"
        )
    elif "linear search" in desc:
        return (
            "def linear_search(arr, target):\n"
            "    for i, val in enumerate(arr):\n"
            "        if val == target:\n"
            "            return i\n"
            "    return -1"
        )
    elif "merge two lists" in desc:
        return (
            "def merge_lists(list1, list2):\n"
            "    return list1 + list2"
        )
    elif "count vowels" in desc:
        return (
            "def count_vowels(s):\n"
            "    return sum(1 for c in s.lower() if c in 'aeiou')"
        )
    elif "capitalize" in desc:
        return (
            "def capitalize_words(s):\n"
            "    return ' '.join(word.capitalize() for word in s.split())"
        )
    else:
        return (
            "# No code generated for this task. Try using keywords like addition, multiplication, swapping, "
            "factorial, palindrome, fibonacci, prime, reverse, sort, gcd, lcm, binary search, linear search, "
            "merge two lists, count vowels")