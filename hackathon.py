import math

def number_spliter(n):
    nums = []
    num_str = str(n)
    i = 0
    while i < len(num_str) // 3:
        nums.append(num_str[len(num_str) - 3 * (i + 1):len(num_str) - 3 * i])
        i += 1

    if len(num_str) % 3 != 0:
        nums.append(num_str[:len(num_str) - (len(num_str) // 3 * 3)])

    nums.reverse()

    return nums

def read_number(n, number_dict):

    # return 'không' -> 'chín' if argument 'n' is in range 0 - 9
    if n >= 0 and n <= 10:
        return number_dict[n]

    # read number in range 10 - 100
    if n > 10 and n < 100:
        if n % 10 == 0:
            return number_dict[n // 10] + ' mươi'

        if n > 10 and n < 20:
            if n % 10 == 5:
                return number_dict[10] + ' lăm'
            return number_dict[10] + ' ' + number_dict[n % 10]
        else:
            if n % 10 == 5:
                return number_dict[int(str(n)[0])] + ' mươi lăm'
            return number_dict[int(str(n)[0])] + ' mươi ' + number_dict[n % 10]

    if n % 100 == 0 and not n % 1000 == 0:
        first_digit = int(str(n)[0])
        return number_dict[first_digit] + ' ' + number_dict[100]

    # read numbers which are divided by 1000, 1000000 or 1000000000
    if n % 1000 == 0 or n % 1000000 == 0 or n % 1000000000 == 0:
        list = number_spliter(n)
        first = int(list[0])

        return read_number(first, number_dict) + ' ' + number_dict[n // first]

    if n > 100 and n < 1000:
        first_digits = int(str(n)[0])                        # Ex: 80000 => 8
        first_digit_text = number_dict[first_digits]          # Ex: 'một', 'hai', ...

        last_digit = int(str(n)[len(str(n)) - 1])           # Ex: 1446 => 6
        last_digit_text = number_dict[last_digit]            # Ex: 'một', 'hai', ...

        unit_num = int(math.pow(10, len(str(n)) - 1))
        unit_text = number_dict[unit_num]

        if (n - last_digit) % unit_num == 0:
            return first_digit_text + ' ' + unit_text + ' linh ' + last_digit_text
        else:
            remaining_num = n - first_digits * unit_num
            return first_digit_text + ' ' + unit_text + ' ' + read_number(remaining_num, number_dict)


def integer_to_vietnamese_numeral(n):
    """ Return the north vietnamese cardinal numeral based on an integer as input

    The function takes an argument 'n' representing a positive integer

    @param n: A positive integer has the maximum value is  999,999,999,999

    @return: The north vietnamese cardinal numeral corresponding to the argument 'n'

    @raise: TypeError if the argument 'n' is not an integer

    @raise: ValueError if the argument 'n' is not a positive integer

    @raise: OverflowError if argument 'n' is over 999,999,999,999
    """

    if not isinstance(n, int):
        raise TypeError('Not an integer')

    if n < 0:
        raise ValueError('Not a positive integer')

    if n > 999999999999:
        raise OverflowError('The value is over')

    number_dict = {
        0: 'không',
        1: 'một',
        2: 'hai',
        3: 'ba',
        4: 'bốn',
        5: 'năm',
        6: 'sáu',
        7: 'bảy',
        8: 'tám',
        9: 'chín',
        10: 'mười',
        100: 'trăm',
        1000: 'nghìn',
        1000000: 'triệu',
        1000000000: 'tỉ'
    }

    if n <= 1000 or n % 100 == 0 or n % 1000 == 0 or n % 1000000 == 0 or n % 1000000000 == 0:
        return read_number(n, number_dict)


    vietnamese_cardinal_numeral = ''

    splited_nums = number_spliter(n)

    for i in range(len(splited_nums)):
        unit = n // int(splited_nums[0])
        if unit != 1000:
            unit //= 1000
            unit *= 1000

        if i == 0:
            vietnamese_cardinal_numeral += read_number(int(splited_nums[i]), number_dict) + ' ' + number_dict[unit] + ' '
        


    return splited_nums


# print(number_spliter(1999))
print(integer_to_vietnamese_numeral(10005))