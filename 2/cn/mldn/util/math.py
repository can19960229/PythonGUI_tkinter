def add(*numbers):
    '''
    实现任意数字的相加操作
    :param number:要进行相加操作的数字内容
    :return:累加的结果
    '''
    num = 0
    for item in numbers:
        num += item
    return num
