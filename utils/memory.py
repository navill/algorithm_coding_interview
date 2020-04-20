import psutil
import os

print("==" * 20)
print("== memory usage check")

for exec_num in range(0, 2):
    ################
    # Input BEFORE code

    ################
    # general RAM usage
    memory_usage_dict = dict(psutil.virtual_memory()._asdict())
    print(memory_usage_dict)
    memory_usage_percent = memory_usage_dict['percent']
    print(f"BEFORE CODE: memory_usage_percent: {memory_usage_percent}%")
    # current process RAM usage
    pid = os.getpid()
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
    print(f"BEFORE CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")
    # del b_var_input_code

    ################
    # Input AFTER  code

    ################
    memory_usage_dict = dict(psutil.virtual_memory()._asdict())
    memory_usage_percent = memory_usage_dict['percent']
    print(f"AFTER  CODE: memory_usage_percent: {memory_usage_percent}%")
    # current process RAM usage
    pid = os.getpid()
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
    print(f"AFTER  CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")
    print("--" * 30)
    # del a_var_input_code
