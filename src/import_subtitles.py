import datetime
import json
import os
import shutil

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
    src = Path(src)
    dest = Path(dest)
    title = Path(title)

    # Get all SRTs
    to_import = []
    failed = []
    for parent, _, files in os.walk(src):
        parent = Path(parent)
        for file in files:
            file = Path(file)

            if file.suffix == '.srt':
                # Only copy files identified as english
                if 'eng' in file.stem.lower() :
                    to_import.append(parent / file)
                else:
                    failed += [file.name]

    # Copy each SRT to the destination folder
    imported = []
    for n, file in enumerate(to_import):
        new_file = Path(dest / f'{title.stem}.eng.{n+1}.srt')
        shutil.copy(file, new_file)
        imported += [(file.name, new_file.name)]

    # log which are imported
    SRTs = {'failed': failed, 'imported': imported}
    with open(SCRIPT_PATH.parent / f'../logs/srts/{NOW}', 'w') as f:
        f.write(json.dumps(SRTs, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()