#!/usr/bin/env python3

import import_subtitles

def main():
	envs = {'RADARR_EVENTTYPE': 'Download',
		'RADARR_MOVIEFILE_SOURCEFOLDER': 'E:\\test', # source
		'RADARR_MOVIE_PATH'            : 'E:\\films\\tick, tick. BOOM! (2021)', # dest
		'RADARR_MOVIEFILE_RELATIVEPATH': 'tick, tick. BOOM! - 2021.mp4'  # new movie filename
	}

	import_subtitles.main(envs)

if __name__ == '__main__':
	main()