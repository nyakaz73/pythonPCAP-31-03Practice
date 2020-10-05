from platform import platform, machine,processor,system,version, python_implementation, python_version_tuple

#Platform General desc
print(platform())
print(platform(1))
print(platform(0,1))

#Returns the machine Generic processor type eg x86_64
print(machine())

#Returns the real processor eg x86_64
print(processor())

#Returns the generic os name eg Linux
print(system())

#Returns the os version
print(version())

#Python Implemntation eg Cython
print(python_implementation())

#Python versoion
for _ in python_version_tuple():
    print(_)


print(__name__)

