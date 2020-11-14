import pickle
import hmac, hashlib
from task import Task
shared_secret = b"super_secret_word"

def create_task():
    task = Task('my_task', 'jump')
    message = pickle.dumps(task)
    digest = hmac.new(key=shared_secret,msg=message, digestmod=hashlib.sha256).digest()
    with open('task.pkl', mode='wb') as f:
        f.write(digest)
        f.write(message)

if __name__ == '__main__':
    create_task()
