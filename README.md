# srttimeadjuster
Simple python program to adjust the time stamps in [SRT subtitle files]( https://en.wikipedia.org/wiki/SubRip#SubRip_text_file_format)


I created this for the occasions when I own a film on DVD without its original (say, French) subtitles: 
I get the subtitles from [some website](http://www.opensubtitles.org/), and they do not match my film because of X seconds before-film logos. 

[VLC](https://en.wikipedia.org/wiki/VLC_media_player) is my player of choice, but it seems not to provide this functionality - so I wrote this simple program. 


My main motivation for writing this, though, was trying out PyQt, and python programming with a non-IDLE IDE, unit tests etc.  

##Run this project

For now, call this in bash: 
```
./run.sh
```

##Run all unit tests

For now, call this in bash: 
```
./run_tests.sh
```

## Special thanks to 

The [PyImports](https://github.com/cod3monk3y/PyImports) Github project for helping me figure out how to work with 
python modules and unit tests. 