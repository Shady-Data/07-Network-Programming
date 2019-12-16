# Subprocess Module
The subprocess module allows us to:
``
spawn new processes
connect to their input/output/error pipes
obtain their return codes
``
It offers a higher-level interface than some of the other available modules, and is intended to replace the following functions:
```
os.system()
os.spawn*()
os.popen*()
popen2.*()
commands.*()
```
We cannot use UNIX commands in our Python script as if they were Python code. For example, echo name is causing a syntax error because echo is not a built-in statement or function in Python. So, in Python script, we're using print name instead.

To run UNIX commands we need to create a subprocess that runs the command. The recommended approach to invoking subprocesses is to use the convenience functions for all use cases they can handle. Or we can use the underlying Popen interface can be used directly.

## os.system()
The simplest way of running UNIX command is to use os.system().
```
>>> import os
>>> os.system('echo $HOME')
/user/root
0

>>> # or we can use
>>> os.system('echo %s' %'$HOME')
/user/root
0
```
As expected, we got $HOME as stdout (to a terminal). Also, we got a return value of 0 which is the result of executing this command, which means there was no error in the execution.

os.system('command with args') passes the command and arguments to our system's shell. By using this can actually run multiple commands at once and set up pipes and input/output redirections. :
```
os.system('command_1 < input_file | command_2 > output_file')
```
If we run the code above os.system('echo $HOME') in the Python IDLE, we only see the 0 because the stdout means a terminal. To see the command output we should redirect it to a file, and the read from it:
```
>>> import os
>>> os.system('echo $HOME > outfile')
0
>>> f = open('outfile','r')
>>> f.read()
'/user/root\n'
```
##  Start a process in Python:

You can start a process in Python using the Popen function call. The program below starts the unix program ‘cat’ and the second parameter is the argument. This is equivalent to ‘cat test.py’.  You can start any program with any parameter.
```python
#!/usr/bin/env python

from subprocess import Popen, PIPE

process = Popen(['cat', 'test.py'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
print stdout
```
The process.communicate() call reads input and output from the process.  
stdout is the process output. stderr will be written only if an error occurs.  If you want to wait for the program to finish you can call Popen.wait().

## Subprocess call():

Subprocess has a method call() which can be used to start a program. 
The parameter is a list of which the first argument must be the program name. The full definition is:
```
subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
# Run the command described by args.
# Wait for command to complete, then return the returncode attribute.
```
In the example below the full command would be “ls -l”
```python
#!/usr/bin/env python

import subprocess
subprocess.call(["ls", "-l"])
```
##  Save process output (stdout)

We can get the output of a program and store it in a string directly using check_output. The method is defined as:
```
 subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)
# Run command with arguments and return its output as a byte string.
```
## Example usage:
```python
#!/usr/bin/env python
import subprocess

s = subprocess.check_output(["echo", "Hello World!"])
print("s = " + s)
```
