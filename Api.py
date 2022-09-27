import os,time,platform
os.system('clear')
print('[•] Checking Updates...')
os.system('git pull')
print('<------------------------------------>')
bit = platform.architecture()[0]
if bit=='64bit':
    print('[•] Congratulations your device support this tool')
    import s
else:
    print('\033[1;31m[×] Sorry Device Not Support')
