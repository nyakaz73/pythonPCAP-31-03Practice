'''
When dealing with files the Unix/Linux OS is case sensive and windows is not
ThisIsTheNameOfTheFile
and
thisisthenameofthefile
Interpreted differently in  Linux but they are the same in windows
'''

'''
IN Linx if you went to access a file you do
var = '/user/file'

but in windows if you do this 
'''
#var = "\user\file" 
'''
you will get an unpleasant result but rather u need to eascape the backslash
var = "\\user\\file"
'''

'''
Fortunately, there is also one more solution. Python is smart enough to be able to convert slashes into backslashes each time it discovers that it's required by the OS.

This means that any the following assignments:

name = "/dir/file"
name = "c:/dir/file"

will work with Windows, too.
'''

# FILE STREAMS
'''There are three basic modes used to open the stream:

read mode: a stream opened in this mode allows read operations only; trying to write to the stream will cause an exception (the exception is named UnsupportedOperation, which inherits OSError and ValueError, and comes from the io module);
write mode: a stream opened in this mode allows write operations only; attempting to read the stream will cause the exception mentioned above;
update mode: a stream opened in this mode allows both writes and reads.
'''

'''
In general, the object comes from one of the classes shown here:

The origin of objects:                              IOBase
                                                /       |           \\
                                        RawIOBase, BufferedIOBase, TextIOBase

Note: you never use constructors to bring these objects to life. The only way you obtain them is to invoke the function named open().

The function analyses the arguments you've provided, and automatically creates the required object.

If you want to get rid of the object, you invoke the method named close().

The invocation will sever the connection to the object, and the file and will remove the object.

For our purposes, we'll concern ourselves only with streams represented by BufferIOBase and TextIOBase objects. You'll understand why soon.
'''
import os

print('abs {}'.format(os.path.dirname(os.path.abspath(__file__))))
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'testfile.txt')


stream = open(my_file,'rt')
print(stream)