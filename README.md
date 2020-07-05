# RGB-HEX Conversor
Converts RGB to Hexadecimal and in reverse. Helpful to converting colors values from one format
to the other.

# Execution

## On Bash
```bash
$ chmod +x rgbtohex
$ ./rgbtohex 255,255,255
#ffffff

$ ./rgbtohex #000000
0,0,0
```

## On Python
```bash
$ python src/main.py 255,255,255
#ffffff

$ python src/main.py #000000
0,0,0
```

# Test
```bash
$ pytest src/*.py
```

# Lint
```bash
$ pylint src/*.py
```
