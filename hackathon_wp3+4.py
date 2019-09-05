import pygame
import time

_number = {
    0: 'không',
    1: 'một',
    2: 'hai',
    3: 'ba',
    4: 'bốn',
    5: 'năm',
    6: 'sáu',
    7: 'bảy',
    8: 'tám',
    9: 'chín'
}

file_names = {
    'không': 'khong',
    'một': 'mot1',
    'mốt': 'mot2',
    'hai': 'hai',
    'ba': 'ba',
    'bốn': 'bon',
    'năm': 'nam',
    'lăm': 'lam',
    'sáu': 'sau',
    'bảy': 'bay',
    'tám': 'tam',
    'chín': 'chin',
    'mười': 'muoi1',
    'mươi': 'muoi2',
    'trăm': 'tram',
    'nghìn': 'nghin',
    'triệu': 'trieu',
    'tỷ': 'ty',
    'ngàn': 'ngan',
    'linh': 'linh',
    'lẻ': 'le'
}


# func to put place value in
def _place_value1(_a, j):
    if j % 3 == 0:
        _a.append('trăm')
    elif (j + 1) % 3 == 0:
        _a.append('mươi')
    return _a


def _place_value2(_a, j, region):
    # Add 'region' parameter to handle 'nghìn' and 'ngàn'
    if j == 4 and region == 'north':
        _a.append('nghìn')
    elif j == 4 and region == 'south':
        _a.append('ngàn')
    elif j == 7:
        _a.append('triệu')
    elif j == 10:
        _a.append('tỷ')
    return _a

def integer_to_vietnamese_numeral(n, region='north', activate_tts = False):
    pygame.init()

    base_dir = './sounds/'

    # check if input have any error
    if type(n) != int:
        raise TypeError("Not an integer")
    elif n < 0:
        raise ValueError("Not a positive integer")
    elif n > 999999999999:
        raise OverflowError("Integer greater than 999,999,999,999")

    elif not isinstance(region, str) and region != None:
        raise TypeError('Argument region is not a string')
    elif region != 'north' and region != 'south':
        raise ValueError('Argument region has not a correct value')
    else:
        _a = list()
        _n = list(str(n))

        i = 0
        j = len(_n)

        while i in range(len(_n)):
            _pas = False
            # special case of #1:
            if int(_n[i]) == 1:
                if i != 0:
                    if (j + 1) % 3 == 0:
                        _a.append('mười')
                        _pas = None
                    elif (j - 1) % 3 == 0:
                        if int(_n[i - 1]) not in (0, 1):
                            _a.append('mốt')
                        else:
                            _a.append(_number[int(_n[i])])
                    else:
                        _a.append(_number[int(_n[i])])
                else:
                    if (j + 1) % 3 == 0:
                        _a.append('mười')
                        _pas = True
                    else:
                        _a.append(_number[int(_n[i])])
            # special case of 5
            elif int(_n[i]) == 5:
                if i != 0 and (j - 1) % 3 == 0 and int(_n[i - 1]) in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                    _a.append('lăm')
                else:
                    _a.append(_number[int(_n[i])])
            # special case of 0
            elif int(_n[i]) == 0:
                if j % 3 == 0:
                    if int(_n[i + 1]) == 0 and int(_n[i + 2]) == 0:
                        _pas = True
                    else:
                        _a.append(_number[int(_n[i])])
                elif (j + 1) % 3 == 0:
                    if int(_n[i + 1]) != 0:
                        # handle 'linh' and 'lẻ'
                        if region == 'north':
                            _a.append('linh')
                        else:
                            _a.append('lẻ')
                        _pas = True
                    else:
                        _pas = True
                elif (j - 1) % 3 == 0:
                    if int(_n[i - 1]) == 0 and int(_n[i - 2]) == 0:
                        _pas = True
                    else:
                        _place_value2(_a, j, region)
                        _pas = True
            else:
                _a.append(_number[int(_n[i])])

            if _pas == False:
                _place_value1(_a, j)

                _place_value2(_a, j, region)
            else:
                pass
            i += 1
            j -= 1

    # play sound files here!
    say_vietnamese_numeral(_a, region)

    _a = ' '.join(_a)

    return (_a)


def say_vietnamese_numeral(list, region = 'north'):
    pygame.init()
    if list == [] or list == None:
        raise ValueError('List is empty or none')

    if region != 'north' and region != 'south':
        raise ValueError('Invalid vietnamese region')

    base_dir = './sounds/' + region + '/'

    if region == 'north':
        for n in list:
            sound_dir = base_dir + file_names[n] + '.ogg'
            pygame.mixer.music.load(sound_dir)
            pygame.mixer.music.play()
            time.sleep(0.8)
    else:

        for n in list:
            sound_dir = base_dir + file_names[n] + '_south.mp3'
            pygame.mixer.music.load(sound_dir)
            pygame.mixer.music.play()
            time.sleep(0.9)


print(integer_to_vietnamese_numeral(1000001, 'south'))
