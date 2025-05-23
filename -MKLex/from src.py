from src.main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello, MKLex!" in captured.out
    def main(): 
        print("Hello, MKLex!")

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello, MKLex!" in captured.out
    def main():
        print("Hello, MKLex!")
from src.main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello, MKLex!" in captured.outœœ





