#!/usr/bin/python3


import argparse
from datetime import datetime
from getpass import getpass
import os
import requests


response = 'request result'
time = 'creation time'
cr_date = 'creation date'


def get_data(username, repo):
    # repo = 'alenaPy/devops_lab'
    global response, time, cr_date
    link = f'https://api.github.com/repos/{repo}/pulls?page=1&per_page=100'
    password = getpass()
    response = requests.get(link, auth=(username, password))
    time = (((response.json()[0]).get('base')).get('repo')).get('created_at')
    cr_date = datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')


def get_arg():

    parser = argparse.ArgumentParser(description='Get PR(Pull \
        Request)statistics from GitHub')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 1.0')
    parser.add_argument('-d', '--days number', action="store_true",
                        dest='d', help='shows number of days opened')
    parser.add_argument('-c', '--creator', action="store_true",
                        dest='c', help='show creation user')
    parser.add_argument('-t', '--time', action="store_true",
                        dest='t', help='returns daytime of creation')
    parser.add_argument('-p', '--pull', action="store_true",
                        dest='p', help='writes PR stats into the file')
    parser.add_argument('-w', '--week', action="store_true",
                        dest='w', help='number of creation week')
    parser.add_argument(metavar='<user>', type=str, dest='user', help='login')
    parser.add_argument(metavar='<repo>', type=str, dest='repo',
                        help='repository on the github.com')
    args = parser.parse_args().__dict__

    return args


def get_days_opened():

    global cr_date
    print(f'Opened {str(datetime.now() - cr_date)[:10]} hours ago')


def get_ow():

    global cr_date
    cr_date = datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')
    print(cr_date)
    cr_week = (cr_date.isocalendar()[1])
    current_week = (datetime.now()).isocalendar()[1]
    difference = current_week - cr_week
    if difference == 1:
        print(f'Created last week({cr_week} week of {str(cr_date)[:4]})')
    else:
        print(f'Created at {cr_week} week of {str(cr_date)[:4]},',
              f'{difference} weeks ago')


def get_creation_time():

    global time
    print("Created at", time[11:16])


def get_creator():

    global response
    owner = ((((response.json()[0]).get('base')).get('repo'))
             .get('owner')).get('login')
    print("Created by", owner)


def get_pull():

    global link, response

    d = input('Input the date(dd-mm-yyyy:)')
    ans = input('Do you want to show pull requests before or after'
                ' the date? (B/A)')

    if not os.path.exists('./output/'):
        os.makedirs('./output/')

    if ans == 'A' or ans == 'After' or ans == 'after':

        for req in response.json():

            if datetime.strptime(d, '%d-%m-%Y') < datetime.strptime(
                    req.get('created_at'), '%Y-%m-%dT%H:%M:%SZ'):
                print(req, file=open("./output/pull_request.json", "a"))

            else:
                break

    elif ans == 'B' or ans == 'Before' or ans == 'before':

        for req in response.json():

            if datetime.strptime(d, '%d-%m-%Y') > datetime.strptime(
                    req.get('created_at'), '%Y-%m-%dT%H:%M:%SZ'):
                print(req, file=open("./output/pull_request.json", "a"))

    else:
        print("Invalid input")
  

def main():

    arg = get_arg()
    get_data(arg['user'], arg['repo'])
    func_dict = {
        'd': 'get_days_opened()',
        'c': 'get_creator()',
        't': 'get_creation_time()',
        'p': 'get_pull()',
        'w': 'get_ow()'
        }

    for i, j in arg.items():

        if j == True:

            exec(func_dict[i])


main()
