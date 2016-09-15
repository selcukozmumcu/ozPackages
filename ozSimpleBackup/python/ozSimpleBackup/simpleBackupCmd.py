import argparse
import simpleBackupLib

#
## @brief Triggers simpleBackupLib from Terminal.
#  
#  @exception N/A
#  
#  @retval None - None.
def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', help='source directory', type=str)
    parser.add_argument('-d', help='destination directory', type=str)
    parser.add_argument('-o','--display', help='displays the absolute path for each copied item', action='store_true')
    
    args = parser.parse_args()
    
    # Optional argument to display copied contents with absolute paths.
    if args.display:
        display=True
    
    try:
        result = simpleBackupLib.simpleBackup(args.s, args.d, display)      
    
    except Exception, error:
        print '\n%s\n' %str(error)
        
if __name__=='__main__':
    main()