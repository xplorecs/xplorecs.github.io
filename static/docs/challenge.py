"""
This generates the project4 ciphertext.
"""

from random import SystemRandom
from lorenz import char_to_baudot, baudot_to_char
from project4_solution import xor, string_to_baudot, baudot_to_string, \
   rotate_wheel, rotate_wheel_by, rotate_wheel_list, rotate_wheel_list_by, wheel_encrypt

"""
These are the wheel lists for the challenge.

A table from https://en.wikipedia.org/wiki/Lorenz_cipher gives the
number of pins for each wheel (which varies).  Note that the table
uses chi-wheels for what we have been calling the K-wheels, mu-wheels
for the M-wheels, and psi-wheels for the S-wheels.

The wheel patterns are based on the BREAM patterns what were actually
used by the Nazis (see
http://practicalcryptography.com/ciphers/lorenz-cipher/).  Although,
things were much tougher than this for the Allies - the patterns used
were changed periodically, and have to be reverse-engineered.

"""

def convert_to_wheel(s):
    return [1 if c == 'x' else 0 for c in s]

KC_wheels = [
    convert_to_wheel('...xxxx....xx....x.xx..x..xx.x.xx.x.xxxx.'), # bk1 
    convert_to_wheel('xx..xxx.xx...x.x.xx...x....xxx.'), # bk2
    convert_to_wheel('..xxx.xx..x....xxx..xx.xx..xx'), # bk3
    convert_to_wheel('..xx..x.xx..x..xx..x..xxxx'), # bk4
    convert_to_wheel('.x...x.xx..x...xxx.xxx.') # bk5
    ]

SC_wheels = [
    convert_to_wheel('..x.x.x.x.x..x..x.xx.xx.x.x..xx.xxx..xxx...'), # bs1
    convert_to_wheel('..x.xx.x.x.x.x.x.xx..xx.x..x.xxxx.....xxx..x.xx'), # bs2
    convert_to_wheel('x.x.x.x.x.x.x..x..xx.x.x.xxxx....xxx...xxx.xx..x..x'), # bs3
    convert_to_wheel('x.x..xx.x.x.x.x.x.xx.x....xx..xx..xx.xxxxx.x..x....x.'), # bs4
    convert_to_wheel('.x.x.x.x.xx...x.x..xxx.xxxx.xx.x....x...x..xx.xx..xx..x.x.x') # bs5
    ]

MC_wheels = [
    convert_to_wheel('xxx.x.xx..xx..xx...xxxx.x.xx.xx...xx....xxxx.xx..xx...xx....x'), # bm1
    convert_to_wheel('x.xxx.x.x.x.x..x.x.xxx.x.x.x.x.x.x.x.') # bm2
    ]

"""
This defines a more realistic Lorenz cipher machine than the one used
in the rest of Project 4.  Unlike the simplified version which uses 1
M-wheel and advances the S-wheels whenever the M-wheel value is 1, it
uses two mwheels, and the swheels advance only when the second M-wheel
is in a 1-position.

NOTE: You should finish your own do_lorenz function before looking at
this code.  It is not the same as what you would need for do_lorenz,
but you should not base your do_lorenz function on this code.
"""

def do_real_lorenz(msg, kwheels, swheels, mwheels):
    """
    Returns the result of encrypting the msg starting from the configuration
    given by the input kwheels, swheels, and mwheels.
    """
    ciphertext = []
    m1wheel = mwheels[0]
    m2wheel = mwheels[1]
    for character in msg:
        ciphertext.append(wheel_encrypt(wheel_encrypt(character, kwheels), swheels))
        kwheels = rotate_wheel_list(kwheels)
        if m2wheel[0] == 1:
            swheels = rotate_wheel_list(swheels)
        m1wheel = rotate_wheel(m1wheel)
        if m1wheel[0]:
            m2wheel = rotate_wheel(m2wheel)
    return ciphertext

def generate_configuration():
    """
    Generates a configuration for the Lorenz machine.
    For each wheel, randomly select a starting position.

    The configuration is a 12-tuple of the starting positions for 
    each wheel (K, S, M wheels in order).
    """
    cryptogen = SystemRandom()
    return [cryptogen.randrange(len(wheel)) for wheel in (KC_wheels + SC_wheels + MC_wheels)]

def configure_wheels(kwheels, swheels, mwheels, configuration):
    assert len(configuration) == len(kwheels) + len(swheels) + len(mwheels)
    K_wheels = [rotate_wheel_by(kwheels[i],
                                configuration[i]) 
                for i in range(len(kwheels))]
    S_wheels = [rotate_wheel_by(swheels[i],
                                configuration[i + len(kwheels)]) 
                for i in range(len(swheels))]
    M_wheels = [rotate_wheel_by(mwheels[i],
                                configuration[i + len(kwheels) + len(swheels)]) 
                for i in range(len(mwheels))]
    return (K_wheels, S_wheels, M_wheels)

def encrypt_message(msg):
    configuration = generate_configuration()
    print("Top secret configuration: " + str(configuration))
    (kw, sw, mw) = configure_wheels(KC_wheels, SC_wheels, MC_wheels, configuration)
    plaintext = string_to_baudot(msg)
    msg2 = baudot_to_string(plaintext)
    if not msg == msg2:
        print("Message contains non-Baudot characters (" \
                 + str(len(msg) - len(msg2)) + " of " + str(len(msg)) + " chars lost)")
    ciphertext = do_real_lorenz(plaintext, kw, sw, mw)
    cmsg = baudot_to_string(ciphertext)
    print (cmsg)
    assert msg2 == decrypt_message(configuration, cmsg)
    return cmsg

def decrypt_message(configuration, cmsg):
    (kw, sw, mw) = configure_wheels(KC_wheels, SC_wheels, MC_wheels, configuration)
    ciphertext = string_to_baudot(cmsg)
    plaintext = do_real_lorenz(ciphertext, kw, sw, mw)
    return baudot_to_string(plaintext)
