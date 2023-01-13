card_number = input("Enter a valid credit card number to check: ")

def is_credit_card_valid(card_number):
    # Reverse the card number
    card_number = card_number[::-1]
    # Convert to a list of ints
    card_number = [int(x) for x in card_number]
    # Double every second digit
    card_number = [x * 2 if i % 2 == 0 else x for i, x in enumerate(card_number)]
    # Subtract 9 from numbers over 9
    card_number = [x - 9 if x > 9 else x for x in card_number]
    # Sum all digits
    total = sum(card_number)
    # Check if total is divisible by 10
    if total % 10 == 0:
        return True
    else:
        return False
if is_credit_card_valid(card_number):
    print("Valid credit card")
else:
    print("Invalid credit card")
