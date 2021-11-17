import os
import shutil

from pathlib import Path

SCRIPT_PATH = Path(__file__)
ENV_FILE = Path(SCRIPT_PATH.parent / 'ARR_ENV.txt')

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
            raise Exception('No *arr Environment variables were found.')

    if 'RADARR_EVENTTYPE' in envs:
        movie = ''

        if len(envs) > 1: # Not a Test
            radarr(envs['RADARR_MOVIEFILE_SOURCEFOLDER'],
                envs['RADARR_MOVIE_PATH'],
                envs['RADARR_MOVIEFILE_RELATIVEPATH']
            )
            movie = ' ' + envs['RADARR_MOVIE_TITLE']


def radarr(src, dest, title):
    src = Path(src)
    dest = Path(dest)
    title = Path(title)

    # Get all SRTs
    for parent, _, files in os.walk(src):
        parent = Path(parent)
        for file in files:
            file = Path(file)

            if file.suffix == '.srt':
                # Only copy files identified as english
                if 'eng' in file.stem.lower() :
                    to_import.append(parent / file)

    # Copy each SRT to the destination folder
    for n, file in enumerate(to_import):
        new_file = Path(dest / f'{title.stem}.eng.{n+1}.srt')
        shutil.copy(file, new_file)


if __name__ == "__main__":
    main()