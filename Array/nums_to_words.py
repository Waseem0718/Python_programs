def number_to_words(n):
    # Define the words for the numbers
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    # Handle zero case
    if n == 0:
        return "Zero"

    # Handle hundreds
    if n >= 100:
        return ones[n // 100] + " Hundred and " + number_to_words(n % 100).strip()

    # Handle teens
    if n >= 10 and n < 20:
        return teens[n - 10]

    # Handle tens and ones
    if n >= 20:
        return tens[n // 10] + " " + ones[n % 10]

    return ones[n]

# Example usage:
number = 433
print(number_to_words(number))