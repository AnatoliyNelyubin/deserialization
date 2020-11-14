import pickle
import hmac, hashlib
shared_secret = b"super_secret_word"

def execute_task():

    with open('task.pkl', 'rb') as f:
        digest = f.read(32)
        message = f.read()
    calculated_digest = hmac.new(key=shared_secret,msg=message, digestmod=hashlib.sha256).digest()
    if hmac.compare_digest(digest,calculated_digest):
        task = pickle.loads(message)
        print(f'Task {task.name} was executed')
        print(f'Result: {task.action}')
    else:
        print("Data in the pickle file is not safe")

if __name__ == '__main__':
    execute_task()
