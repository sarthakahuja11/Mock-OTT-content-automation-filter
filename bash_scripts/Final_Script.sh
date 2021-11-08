Final Script		
#!/bin/bash																		
 
####(Add script in folder <ChannelName> )																		
mkdir converted																		
youtube-dl --match-filter 'duration > 59 & duration < 451' -ciw -o "%(title)s.%(ext)s" -v 'http://www.abcdef.com/playlist?list=UUHfEG_8gLhsv8aALrWJfN4g'      ##download > 59 secs but < 451 secs																		

for f in *																		
do																		
ffmpeg -i "$f" -ss 00:00:10.000 -vframes 1 "converted/${f%.*}.png"																		
duration=$(ffprobe -v quiet -of csv=p=0 -show_entries format=duration "$f")																		
duration1=${duration%.*}																		
if [ "$duration1" -le 300 ]; then																		
if [[ "$f" == *.mp4 ]]; then																		
echo "COPYING DIRECTLY **************************************************************************"																		
mv "$f" "converted/$f"																		
else																		
echo "CONVERTING TO MP4 **************************************************************************"																		
ffmpeg -i "$f"  -crf 24 "converted/${f%.*}.mp4"																		
rm "$f"																		
fi																		
else																		
echo "SPEED UP ***************************************************************************************"																		
ffmpeg -i "$f" -filter_complex "[0:v]setpts=0.67*PTS[v];[0:a]atempo=1.5[a]" -map "[v]" -map "[a]" -crf 24 "converted/${f%.*}.mp4"        ##speedup ##auto convert																		
if [[ "$f" != *.sh ]]; then																				rm "$f"																		
fi																		
fi																		
done																		
 
															