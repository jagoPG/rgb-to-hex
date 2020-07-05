from conversor import rgb_to_hex, hex_to_rgb
from validator import is_hex, is_rgb

def test_is_hex():
    assert is_hex('#ae3211') == True
    assert is_hex('#ffa21f') == True
    assert  is_hex('#ffa21fc') == False

def test_is_rgb():
    assert is_rgb('255,255,255') == True
    assert is_rgb('25,255,137') == True
    assert is_rgb('1,25,135') == True
    assert is_rgb(',25,135') == False
    assert is_rgb('353,25,135') == False
    assert is_rgb('2,256,135') == False
    assert is_rgb('2,256,1354') == False

def test_rgb_to_hex():
    assert rgb_to_hex('255,255,255') == '#ffffff'
    assert rgb_to_hex('0,0,0') == '#000000'
    assert rgb_to_hex('4,54,123') == '#04367b'
    assert rgb_to_hex('129,1,4') == '#810104'

def test_hex_to_rgb():
    assert hex_to_rgb('#ffffff') == '255,255,255'
    assert hex_to_rgb('#000000') == '0,0,0'
    assert hex_to_rgb('#e0dede') == '224,222,222'
    assert hex_to_rgb('#64DD42') == '100,221,66'
