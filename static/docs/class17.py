"""
class17.py

cs1120 Spring 2016
"""

def mba_add(a, b):
    if b == 0:
        return a
    else:
        return 1 + mba_add(a, b - 1)

def mba_add(a, b):
    for _ in range(b):
        a = a + 1
    return a

def generate_addition_table():
    entries = []
    for a in range(10):
        for b in range(10):
            val = (a + b) % 10
            carry = (a + b) > 10
            entries.append("('" + str(a) + "', '" +
                           str(b) + "'): ('" +
                           str(val) + "', " +
                           str(carry) + ")")
    return "{" + ', '.join(entries) + "}"

ADDITION_TABLE = {
    ('0', '0'): ('0', False), ('0', '1'): ('1', False),
    ('0', '2'): ('2', False), ('0', '3'): ('3', False),
    ('0', '4'): ('4', False), ('0', '5'): ('5', False),
    ('0', '6'): ('6', False), ('0', '7'): ('7', False),
    ('0', '8'): ('8', False), ('0', '9'): ('9', False),
    ('1', '0'): ('1', False), ('1', '1'): ('2', False),
    ('1', '2'): ('3', False), ('1', '3'): ('4', False),
    ('1', '4'): ('5', False), ('1', '5'): ('6', False),
    ('1', '6'): ('7', False), ('1', '7'): ('8', False),
    ('1', '8'): ('9', False), ('1', '9'): ('0', False),
    ('2', '0'): ('2', False), ('2', '1'): ('3', False),
    ('2', '2'): ('4', False), ('2', '3'): ('5', False),
    ('2', '4'): ('6', False), ('2', '5'): ('7', False),
    ('2', '6'): ('8', False), ('2', '7'): ('9', False),
    ('2', '8'): ('0', False), ('2', '9'): ('1', True),
    ('3', '0'): ('3', False), ('3', '1'): ('4', False),
    ('3', '2'): ('5', False), ('3', '3'): ('6', False),
    ('3', '4'): ('7', False), ('3', '5'): ('8', False),
    ('3', '6'): ('9', False), ('3', '7'): ('0', False),
    ('3', '8'): ('1', True), ('3', '9'): ('2', True),
    ('4', '0'): ('4', False), ('4', '1'): ('5', False),
    ('4', '2'): ('6', False), ('4', '3'): ('7', False),
    ('4', '4'): ('8', False), ('4', '5'): ('9', False),
    ('4', '6'): ('0', False), ('4', '7'): ('1', True),
    ('4', '8'): ('2', True), ('4', '9'): ('3', True),
    ('5', '0'): ('5', False), ('5', '1'): ('6', False),
    ('5', '2'): ('7', False), ('5', '3'): ('8', False),
    ('5', '4'): ('9', False), ('5', '5'): ('0', False),
    ('5', '6'): ('1', True), ('5', '7'): ('2', True),
    ('5', '8'): ('3', True), ('5', '9'): ('4', True),
    ('6', '0'): ('6', False), ('6', '1'): ('7', False),
    ('6', '2'): ('8', False), ('6', '3'): ('9', False),
    ('6', '4'): ('0', False), ('6', '5'): ('1', True),
    ('6', '6'): ('2', True), ('6', '7'): ('3', True),
    ('6', '8'): ('4', True), ('6', '9'): ('5', True),
    ('7', '0'): ('7', False), ('7', '1'): ('8', False),
    ('7', '2'): ('9', False), ('7', '3'): ('0', False),
    ('7', '4'): ('1', True), ('7', '5'): ('2', True),
    ('7', '6'): ('3', True), ('7', '7'): ('4', True),
    ('7', '8'): ('5', True), ('7', '9'): ('6', True),
    ('8', '0'): ('8', False), ('8', '1'): ('9', False),
    ('8', '2'): ('0', False), ('8', '3'): ('1', True),
    ('8', '4'): ('2', True), ('8', '5'): ('3', True),
    ('8', '6'): ('4', True), ('8', '7'): ('5', True),
    ('8', '8'): ('6', True), ('8', '9'): ('7', True),
    ('9', '0'): ('9', False), ('9', '1'): ('0', False),
    ('9', '2'): ('1', True), ('9', '3'): ('2', True),
    ('9', '4'): ('3', True), ('9', '5'): ('4', True),
    ('9', '6'): ('5', True), ('9', '7'): ('6', True),
    ('9', '8'): ('7', True), ('9', '9'): ('8', True)}

NEXT_DIGIT = {'0': '1', '1': '2', '2': '3', '3': '4',
              '4': '5', '5': '6', '6': '7',
              '7': '8', '8': '9'}

def add_one(a, b, carry):
    value, newcarry = ADDITION_TABLE[(a, b)]
    if carry:
        if value == '9':
            value = '0'
            assert not newcarry
            newcarry = True
        else:
            value = NEXT_DIGIT[value]
    return value, newcarry
    
def thirdgrade_add(a, b):
    adigits = [digit for digit in list(str(a))]
    bdigits = [digit for digit in list(str(b))]
    adigits.reverse()
    bdigits.reverse()
    maxlen = max(len(adigits), len(bdigits))
    while len(adigits) < maxlen:
        adigits.append('0')         
    while len(bdigits) < maxlen:
        bdigits.append('0') 
    assert len(adigits) == len(bdigits)
    # print("Adding: " + str(adigits) + " + " + str(bdigits))
    result = []
    carry = False
    for digits in zip(adigits, bdigits):
        value, carry = add_one(digits[0], digits[1], carry)
        result.append(value)
    if carry:
        result.append('1')
    result.reverse()
    return ''.join(result)



