import datetime
import json
import os

from pathlib import Path

SCRIPT_PATH = Path(__file__)
ENV_FILE = Path(SCRIPT_PATH.parent / 'ARR_ENV.txt')
NOW = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')

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
            log_envs(envs)
            raise Exception('No *arr Environment variables were found.')

    log_envs(envs)

    if 'RADARR_EVENTTYPE' in envs:
        if len(envs) > 1: # Not a Test
            radarr(envs['RADARR_MOVIEFILE_SOURCEFOLDER'],
                envs['RADARR_MOVIE_PATH'],
                envs['RADARR_MOVIEFILE_RELATIVEPATH']
            )


def log_envs(envs):
    with open(SCRIPT_PATH.parent / f'../logs/envs/{NOW}', 'w') as f:
        f.write(json.dumps(envs, indent=4, sort_keys=True))


def radarr(src, dest, title):
    # Check if src has any SRT files
    # Import them (all?)
    pass


if __name__ == "__main__":
    main()