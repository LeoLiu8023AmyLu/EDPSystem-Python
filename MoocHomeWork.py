'''
Created on 2016年11月17日

@author: Anshare_LY
'''
     
if __name__ == '__main__':
    while True:
        inputwords = input('Input:')
        for var in inputwords:
            if (ord(var) in range(97, 122)):
                if(ord(var)<110):print(chr(ord(var)+13),end='')
                else:print(chr(ord(var)-13),end='')
            elif (ord(var) in range(65, 91)):
                if(ord(var)<78):print(chr(ord(var)+13),end='')
                else:print(chr(ord(var)-13),end='')
            else: print(var,end='')
        print()

            
            
    