#!/usr/bin/env python3

import import_subtitles

def main():
	envs = {'RADARR_EVENTTYPE': 'Download',
		'RADARR_MOVIEFILE_SOURCEFOLDER': 'D:\\T\\T\\Sansho.the.Bailiff.1954.JAPANESE.1080p.BluRay.H264.AAC-VXT', # source
		'RADARR_MOVIE_PATH'            : 'E:\\films\\Sansho the Bailiff (1954)', # dest
		'RADARR_MOVIEFILE_RELATIVEPATH': 'Sansho the Bailiff - 1954.mp4'  # new movie filename
	}

	import_subtitles.main(envs)

if __name__ == '__main__':
	main()