from nose.tools import *
from mcpi import mc_pi

print(mc_pi.approx_pi())

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!")
