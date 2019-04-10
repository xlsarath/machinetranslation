# Machine Translation

This is a project developed to machine translate the videos with English audio to videos in Regional Languages. Currently only some Indian Languages are implemented.


How it works :

1) Input video is splitted into 15 different constituents with respect to audio frequency .
2) a copy of muted video is saved for later usage
3) Audio is fed to IBM watson in 15 parallel threads
4) Response is captured and fed to google translate API, where raw text converted to regional language text
5) Translated text is converted into audio by TTS module/ FLite engine
6) Now audio is stiched back to Video for playback.
