import sys
import argparse
import json
import hashlib
import os
from pprint import pprint
import datetime

def get_arguments(created=False, hash_required=True, when=False):
    ap = argparse.ArgumentParser(prog=sys.argv[1])
    ap.add_argument('type')
    if created:
        ap.add_argument('-n', '--name', help='Name of task', required=True)
        ap.add_argument('-D', '--deadline',
                        help='Deadline of task', required=True)
        ap.add_argument('-d', '--description',
                        help='Description of task', required=True)
    if hash_required:
        ap.add_argument('task_hash')
    if when:
        ap.add_argument('when')
    args = vars(ap.parse_args())
    del args['type']
    return args


def read_tasks():
    with open('tasks.json') as tasks_file:
        tasks = json.load(tasks_file)
    return tasks


def save_tasks(tasks):
    with open('tasks.json', 'w') as tasks_file:
        json.dump(tasks, tasks_file)

def format_date(date):
    return str(datetime.datetime.strptime(date, '%Y-%m-%d').date())

def add_task():
    tasks = read_tasks()
    task = get_arguments(created=True, hash_required=False)
    task['deadline'] = format_date(task['deadline'])
    task_hash = hashlib.sha1(json.dumps(task).encode()).hexdigest()
    tasks[task_hash] = task
    save_tasks(tasks)


def delete_task():
    tasks = read_tasks()
    task = get_arguments()
    del tasks[task['task_hash']]
    save_tasks(tasks)


def update_task():
    tasks = read_tasks()
    task = get_arguments(created=True)
    task_hash = task['task_hash']
    if task_hash in tasks.keys():
        actual_task = tasks[task_hash]
        for key in task.keys():
            if key != '*':
                actual_task[key] = task[key]
        tasks[task_hash] = actual_task
        save_tasks(tasks)
    else:
        print('Task does not exist')


def list_tasks():
    tasks = read_tasks()
    args = get_arguments(hash_required=False, when=True)
    if args['when'] == 'all':
        pprint(tasks)
    elif args['when'] == 'today':
        to_print = {}
        for task_hash, task in tasks.items():
            if task['deadline'] == str(datetime.datetime.today().date()):
                to_print[task_hash] = task
        pprint(to_print)
                


if __name__ == '__main__':
    if not os.path.exists('tasks.json'):
        with open('tasks.json', 'w') as tasks_file:
            tasks = json.dump({}, tasks_file)

    if sys.argv[1] == 'add':
        add_task()
    elif sys.argv[1] == 'delete':
        delete_task()
    elif sys.argv[1] == 'list':
        list_tasks()
    elif sys.argv[1] == 'update':
        update_task()
    else:
        print('function not exist')
