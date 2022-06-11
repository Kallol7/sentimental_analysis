import sys, os

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


# print 'This will print'

# blockPrint()
# print "This won't"

# enablePrint()
# print "This will too"