import sys

def printMatrix(graph):
	for row in range(4):
		for col in range (4):
			print "[" + str("0x%02x" % graph[row][col]) + "]",
		print ""
	print ""
# end printMatrix


def printHex(byte):
	print "0x%02x" % byte


def printHexList(l):
	print "[",
	for i in range(len(l) - 1):
		byte = "0x%02x" % l[i]
		print str(byte) + ",",

	print "0x%02x" % l[len(l) - 1],
	print "]"
# end printHexList


def printHexString(l):
	for i in range(len(l)):
		byte = "%02x" % l[i]
		print str(byte),
	print ""
# end printHexString
