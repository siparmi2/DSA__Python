"""

Have the function RomanNumeralReduction(str) read str which will be a string of Roman numerals in decreasing order. The numerals being used are:
I for 1, V for 5, X for 10, L for 50, C for 100, D for 500, and M for 1000.

Your program should return the same number given by str using a smaller set of Roman numerals.

For example:

If str is "LLLXXXVVVV", this is 200, so your program should return "CC" because this is the shortest way to write 200 using the Roman numeral
system given above.

If a string is given in its shortest form, just return that same string.

"""

def roman_to_int(s):
    """Converts Roman numeral to integer."""
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    for char in s:
        total += roman_map[char]

    return total


def int_to_roman(num):
    """Converts integer back to shortest Roman numeral form."""
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    result = ""
    for i in range(len(val)):
        while num >= val[i]:
            num -= val[i]
            result += syms[i]

    return result


def RomanNumeralReduction(s):
    # Step 1: Convert Roman to Integer
    total = roman_to_int(s)

    # Step 2: Convert Integer back to Shortest Roman form
    return int_to_roman(total)


# ✅ Test cases
print(RomanNumeralReduction("LLLXXXVVVV"))  # Output: "CC"
print(RomanNumeralReduction("XXX"))  # Output: "XXX" (already shortest)
print(RomanNumeralReduction("IIIII"))  # Output: "V"
print(RomanNumeralReduction("VVVV"))  # Output: "XX"
