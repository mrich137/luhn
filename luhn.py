import sys
def luhn(card_number):
    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1
    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not ((count & 1) ^ oddeven):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ((sum % 10) == 0)


def main():
    """ Main function for module debug """

    cc = raw_input('Enter a credit card number: ')

    if(luhn(str(cc))):
        print "CC # is VALID!"
    else:
        print "CC # is INVALID!"

if __name__ == '__main__':
    main()