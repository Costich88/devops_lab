import json
import os
import subprocess
import yaml


def jout():
    jOut = json.dumps(output)
    print(jOut, file=open("output.json", "a"))


def yout():
    yOut = yaml.dump(output)
    print(yOut, file=open("output.yaml", "a"))


def shell_com(command):
    p = subprocess.Popen(command.split(),
                         stdout=subprocess.PIPE)
    preprocessed, _ = p.communicate()
    return preprocessed


def get_version():
    return str(shell_com('python --version'))[2:-3]


def get_ve():
    return os.environ['VIRTUAL_ENV']


def get_exe():
    return str(shell_com('which python'))[2:-3]


def get_pip():
    return str(shell_com('which pip'))[2:-3]


def get_versions():
    return str(shell_com('pyenv versions'))[2:-3]


def get_path():
    # return(str(shell_com('echo $PYTHONPATH'))[2:-3])
    com = 'echo $PYTHONPATH'
    p = subprocess.Popen(com, shell=True,
                         stdout=subprocess.PIPE)
    preprocessed, _ = p.communicate()
    return str(preprocessed)[2:-3]


def get_packages():
    r = str(shell_com('pip list'))[1:]
    r = r.split(r'\n')

    del r[0:2], r[-1]
    for i in range(len(r)):
        r[i] = r[i].split()[0]
    return r


sitepack = {}


def get_site_packages(package_name):
    # com = (f'pip show {package_name} --verbose | grep Home-page')
    com = 'pip show {} --verbose | grep Home-page'.format(package_name)
    p = subprocess.Popen(com, shell=True,
                         stdout=subprocess.PIPE)
    preprocessed, _ = p.communicate()
    sitepack[package_name] = str(preprocessed)[13:-3]


for j in get_packages():
    get_site_packages(j)

output = {'py_version': get_version(),
          'virt_env': get_ve(),
          'py_exe_loc': get_exe(),
          'pip_location': get_pip(),
          'pythonpath': get_path(),
          'pip_packages': get_packages(),
          'web_packages': sitepack, }
        # 'python_versions': get_versions()


jout()
yout()
