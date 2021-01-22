# Simple task list in python
interface: \
python tasks.py add --name Cleaning [--deadline DATETIME] [--description DESCRIPTION]\
python tasks.py update [--name Cleaning] [--deadline DATETIME] [--description DESCRIPTION] TASK_HASH\
python tasks.py remove TASK_HASH\
python tasks.py list [--all | --today]
