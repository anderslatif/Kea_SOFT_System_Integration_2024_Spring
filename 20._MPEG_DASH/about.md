https://sample-videos.com/

```bash 
$ ffmpeg -i input.mp4 -map 0 -c:v libx264 -c:a aac -b:v:0 500k -s:v:0 640x360 -b:v:1 1000k -s:v:1 1280x720 -b:a 128k -adaptation_sets "id=0,streams=v id=1,streams=a" -f dash playlist.mpd
```

