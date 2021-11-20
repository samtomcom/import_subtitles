#!/usr/bin/env python3

import os
import shutil

from pathlib import Path

# Array of tuples in the form ('Language name', 'ISO 639-2/B', 'ISO 639-1')
# https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
LANGS = [('english', 'eng', 'en')]
# For example:
# LANGS = [('english', 'eng', 'en'),
#     ('french', 'fre', 'fr'),
#     ('german', 'ger', 'de')]

def main(envs=None):
    # No environment variables provided for testing, use actual variables
    if not envs: 
        envs = _get_envs()

    if len(envs) == 0 or 'RADARR_EVENTTYPE' not in envs:
        raise Exception('No Radarr environment variables were found')

    # Implies the script was called by Radarr as a Test.
    if len(envs) == 1:
        return

    src = Path(envs['RADARR_MOVIEFILE_SOURCEFOLDER'])
    dest = Path(envs['RADARR_MOVIE_PATH'])
    title = Path(envs['RADARR_MOVIEFILE_RELATIVEPATH']).stem

    # Get all SRTs
    to_import = []
    srts = []
    for parent, _, files in os.walk(src):
        parent = Path(parent)

        for file in files:
            file = Path(parent / file)
            if file.suffix != '.srt':
                pass

            # Save srt files here
            srts += [file]

    _process_srts(srts, src, dest, title)

# Checking all potentiall environment variables
def _get_envs():
    envs = {}
    with open(Path(Path(__file__).parent / 'ARR_ENV.txt'), 'r') as f:
        for line in f:
            env = line.rstrip()
            if env in os.environ:
                envs[env] = os.environ[env]

    return envs

def _process_srts(srts, src, dest, title):
    lang_count    = {b: 0 for _,b,_ in LANGS} # {'eng': 0, 'fre': 0}
    lang_names    = {a: b for a,b,_ in LANGS} # {'english': 'eng', 'french': 'fre'}
    lang_2_letter = {c: b for _,b,c in LANGS} # {'en': 'eng', 'fr': 'fre'}

    # index of SRTs that have been processed, these are skipped once processed
    done = []

    # Name matches
    for lang_name, code in lang_names.items():
        for n, file in enumerate(srts):
            if n in done:
                continue

            if lang_name in file.stem.lower():
                lang_count[code] += 1
                done += [n]
                _copy_file(file, src, dest, title, code, lang_count[code])

    # 3 letter code matches
    for code in lang_count:
        for n, file in enumerate(srts):
            if n in done:
                continue

            if code in file.stem.lower():
                lang_count[code] += 1
                done += [n]
                _copy_file(file, src, dest, title, code, lang_count[code])

    # 2 letter code matches
    for lang_2, code in lang_2_letter.items():
        for n, file in enumerate(srts):
            if n in done:
                continue

            if lang_2 in file.stem.lower():
                lang_count[code] += 1
                done += [n]
                _copy_file(file, src, dest, title, code, lang_count[code])


def _copy_file(file, src, dest, title, code, count):
    new_file = Path(dest / f'{title}.{code}.{count}.srt')
    shutil.copy(src / file, new_file)


if __name__ == "__main__":
    main()