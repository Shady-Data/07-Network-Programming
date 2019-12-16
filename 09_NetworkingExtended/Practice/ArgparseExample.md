# Argparse Module

## Example
The following code is a Python program that takes a list of integers and produces either the sum or the max:
```python
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
```
Assuming the Python code above is saved into a file called prog.py, 
it can be run at the command line and provides useful help messages:
```
$ python prog.py -h
usage: prog.py [-h] [--sum] N [N ...]

Process some integers.

positional arguments:
 N           an integer for the accumulator

optional arguments:
 -h, --help  show this help message and exit
 --sum       sum the integers (default: find the max)
 ```
When run with the appropriate arguments, it prints either the sum or the max of the command-line integers:
```
$ python prog.py 1 2 3 4
4

$ python prog.py 1 2 3 4 --sum
10
```
