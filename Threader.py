import multiprocessing
import time
import random

# Simulating your key jumps
def simulate_key_jumps():
    key_positions = range(6)  # 6 possible key positions
    while True:
        new_pos = random.choice(key_positions)
        print(f'Key jumped to position {new_pos}')
        time.sleep(random.randint(0, 30))  # key stays at the position for 0-30 seconds

# Simulating your pentesting process
def pentest_key_position(position):
    while True:
        print(f'Process {position} checking for key...')
        # Here you'd put the logic to test if the key is at this position
        time.sleep(1)  # Let's say it takes 1 second to check

if __name__ == '__main__':
    key_simulation_process = multiprocessing.Process(target=simulate_key_jumps)
    key_simulation_process.start()

    pentest_processes = []
    for i in range(6):  # Creating a process for each potential key position
        p = multiprocessing.Process(target=pentest_key_position, args=(i,))
        p.start()
        pentest_processes.append(p)

    key_simulation_process.join()
    for p in pentest_processes:
        p.join()
