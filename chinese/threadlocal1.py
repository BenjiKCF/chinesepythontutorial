# coding: utf-8
# 在多線程環境下，每個線程都有自己的數據。
# 一個線程使用自己的局部變量比使用全局變量好，
# 因為局部變量只有線程自己能看見，不會影響其他線程，
# 而全局變量的修改必須加鎖。
import threading

global_dict = {}

def process_student(name):
    std = Student(name)
    # std是局部變量，但是每個函數都要用它，因此必須傳進去：
    global_dict[threading.current_thread()] = std
    do_task_1(std)
    do_task_2(std)

def do_task_1():
    # 不傳入std，而是根據當前線程查找：
    std = global_dict[threading.current_thread()]
    do_subtask_1(std)
    do_subtask_2(std)

def do_task_2():
    # 任何函數都可以查找出當前線程的std變量：
    std = global_dict[threading.current_thread()]
    do_subtask_1(std)
    do_subtask_2(std)
