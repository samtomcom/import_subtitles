#!/usr/bin/env python3

import os
import shutil

from pathlib import Path

ENV_FILE = Path(Path(__file__).parent / 'ARR_ENV.txt')

def main(envs=None):
    # No environment variables provided for testing, use actual variables
    if not envs: 
        # Checking all potentiall environment variables
        envs = {}
        with open(ENV_FILE, 'r') as f:
            for line in f:
                env = line.rstrip()
                if env in os.environ:
                    envs[env] = os.environ[env]

    if len(envs) == 0 or 'RADARR_EVENTTYPE' not in envs:
        raise Exception('No Radarr environment variables were found')

    # Implies the script was called by Radarr as a Test.
    if len(envs) == 1:
        return

    src = Path(envs['RADARR_MOVIEFILE_SOURCEFOLDER'])
    dest = Path(envs['RADARR_MOVIE_PATH'])
    title = Path(envs['RADARR_MOVIEFILE_RELATIVEPATH'])

    # Get all SRTs
    to_import = []
    for parent, _, files in os.walk(src):
        parent = Path(parent)

        for file in files:
            file = Path(file)

            if file.suffix != '.srt':
                pass

            # Only copy files identified as english
            if 'eng' in file.stem.lower() :
                to_import.append(parent / file)
            else:
                pass

    # Copy each SRT to the destination folder
    for n, file in enumerate(to_import):
        new_file = Path(dest / f'{title.stem}.eng.{n+1}.srt')
        shutil.copy(file, new_file)


if __name__ == "__main__":
    main()