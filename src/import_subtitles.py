import datetime
import json
import os

SCRIPT_PATH = os.path.realpath(__file__)
SCRIPT_DIR = os.path.dirname(SCRIPT_PATH)
ENV_FILE = f'{SCRIPT_DIR}\\ARR_ENV.txt'

def main():
    envs = {}

    # Checking all potentiall environment variables
    with open(ENV_FILE, 'r') as f:
        for line in f:
            env = line.rstrip()
            if env in os.environ:
                envs[env] = os.environ[env]

        # No environment variables were found
        # Either the script was run manually as a test (ie Not ran by *arr)
        #  or, something went wrong : )
        if len(envs) == 0:
            envs = {'Custom': 'Test'}
            log(envs)
            raise Exception('No *arr Environment variables were found.')

    log(envs)


def log(envs):
    with open(f'{SCRIPT_DIR}\\logs\\{datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")}', 'w') as f:
        f.write(json.dumps(envs))


if __name__ == "__main__":
    main()