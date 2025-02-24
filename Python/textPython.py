import sys
import time
if __name__ == '__main__':
    sys.stdout = sys.__stdout__
    print('Starting')
    time.sleep(1)
    print('After 1s : Test, args : ')
    for arg in sys.argv[1:]:
        print(arg)