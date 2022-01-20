import subprocess

if __name__ == '__main__':
    #rs = subprocess.run('behave -k -t f1s1 --no-capture',shell=True, check=True)
    rs = subprocess.run('behave -k --no-capture',shell=True, check=True)
