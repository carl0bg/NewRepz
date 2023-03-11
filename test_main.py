from main import main

def test_main():
    assert main(2, 3) == 5

def test_main_2():
    assert main(3, 3) == 6
