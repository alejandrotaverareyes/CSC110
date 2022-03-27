### 
### Author: Alejandro Tavera-Reye
### Description: adjadoOLD
###              


def main():
    Castle_Width = input("Castle width: \n")
    Shadow_Width = int(Castle_Width) * ' '
    Castle_Bricks = int(Castle_Width) * '_'

    print("   " + Shadow_Width + ".-.-.")
    print('[-]' + Shadow_Width + '|-.-|' + Shadow_Width + '[-]')
    print("| |" + Castle_Bricks + '| H |'+ Castle_Bricks + '| |')
    print('| |' + Shadow_Width + '| H |' + Shadow_Width + '| |')
    print('| |' + Shadow_Width + '| H |' + Shadow_Width + '| |')
    print("|_|" + Castle_Bricks + '| H |'+ Castle_Bricks + '|_|')

main()