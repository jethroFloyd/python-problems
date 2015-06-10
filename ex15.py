from sys import argv

script, filename = argv

txt = open(filename)
print "The file is this: %r" %filename
print txt.read()
txt.close()
