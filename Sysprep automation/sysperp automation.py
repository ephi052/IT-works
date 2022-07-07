import os


def try_prep():
    '''This function try to run sysprep(generalize)and shutdown the system'''
    os.system('C:\Windows\System32\Sysprep\Sysprep.exe /generalize /shutdown /oobe')


def get_lines_from_log_file():
    file_path = 'C:\Windows\System32\Sysprep\Panther\setupact.log'
    lines = open(file_path).readlines()
    return lines


def get_erorr_line_number(lines):
    last_try = lines[-30:]
    line_number = 1
    for line in last_try:
        print('[', line_number, ']', line)
        line_number = line_number + 1
    error_line = int(input('>> please enter the first Error line number: '))
    line = last_try[error_line-1]
    print('\n>> selected line is ', line)
    return error_line-1


def get_error_line(lines, line_number):
    last_try = lines[-30:]
    line_number = abs(line_number)
    return last_try[line_number]


def pars_line(line):
    slpited_line = line.split()
    if slpited_line[4] == 'Package':
        pkg_name = slpited_line[5]
        print('>> package name')
        print(pkg_name)
        return pkg_name
    else:
        print(
            'selected line not correct or it is not package problem check Log file'
        )
        exit()


def remove_pkg(pkg_name):
    os.system('powershell.exe Remove-AppxPackage -allusers -Package "'+pkg_name+'"')
    print('\n'+pkg_name+' removed')


try_prep()
line_number = get_erorr_line_number(get_lines_from_log_file())


for i in range(2):
    try_prep()
    pkg_name = pars_line(get_error_line(get_lines_from_log_file(),line_number))
    remove_pkg(pkg_name)
