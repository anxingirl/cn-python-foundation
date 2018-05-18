"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""

def add_to_set(phone_list =[]):
    """
    Return the phone numbers list
    Args:
        phone_list(list): the list of phone communications.
        The first  and second string of every record are phone number.
        ['78130 00821', '98453 94494', '01-09-2016 06:01:12', '186']
    Return:
        phone_num(set):set of phone numbers concated from  the first and second string of every record
    """
    phone_set = set()
    for phone in phone_list:
        phone_set.add(phone[0])
        phone_set.add(phone[1])
    return phone_set
phone_set1 = add_to_set(calls)
phone_set2 = add_to_set(texts)
print("There are {} different telephone numbers in the records.".format(len(phone_set1 | phone_set2)))
