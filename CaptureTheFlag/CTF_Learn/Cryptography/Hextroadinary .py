# Full url to this task: https://ctflearn.com/challenge/158
# Youtube Conversion Video: https://www.youtube.com/watch?v=ZL-LhaaMTTE
# XOR Operation: https://pl.wikipedia.org/wiki/Alternatywa_roz%C5%82%C4%85czna

#  0xc4115      0x4cf8
# 803 093       19704

firstHexValue = 0xc4115
secondHexValue = 0x4cf8

xorTwoBinaryNumbers = bin(firstHexValue ^ secondHexValue)
hexValue = hex(int(xorTwoBinaryNumbers,2))
print(hexValue)