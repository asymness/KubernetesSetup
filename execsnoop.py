from subprocess import Popen, PIPE, STDOUT
import csv

def parse(line):
    line = line.strip()
    line = line.split(" ")
    pid = line.pop(0)
    while not pid:
        pid = line.pop(0)
    ppid = line.pop(0)
    while not ppid:
        ppid = line.pop(0)
    line = ' '.join(line)
    cmd = line.strip()
    return pid, ppid, cmd

i = 0
with open("logs.csv", "w+") as f:
    writer = csv.writer(f)
    p = Popen('./execsnoop', stdout = PIPE, 
        stderr = STDOUT)
    while p.poll() is None:
        i += 1
        line = p.stdout.readline()
        if i < 3:
            continue
        pid, ppid, cmd = parse(line)
        writer.writerow([pid, ppid, cmd])
