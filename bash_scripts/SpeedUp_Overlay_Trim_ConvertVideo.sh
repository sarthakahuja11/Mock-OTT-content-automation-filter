Speed_conv_overlay_trim	Linux	
 
#!/bin/bash																		
 
mkdir converted_speed																		
cp wLogo3.png converted_speed																		
 
for f in *.mp4																		
do																		
duration=$(ffprobe -v quiet -of csv=p=0 -show_entries format=duration "$f")																		
duration1=${duration%.*}																		
if [ "$duration1" -le 450 ]; then																		
echo "SPEED UP****************************************************************************************"																		
ffmpeg -i "$f" -filter_complex "[0:v]setpts=0.67*PTS[v];[0:a]atempo=1.5[a]" -map "[v]" -map "[a]" -crf 24 "converted_speed/${f%.*}.mp4"																		
fi																		
done																		
 
cd converted_speed																		
mkdir overlay																		

for j in *.mp4;																		
do																		
ffmpeg -i "$j" -i wLogo3.png -filter_complex "[0:v][1:v] overlay=W-w-80:H-h-25:" -pix_fmt yuv420p -c:a copy "overlay/$j"																		
done																		

cd overlay																		
mkdir output																		

for e in *.mp4; do																		
cut_duration=10																		
input_duration=$(ffprobe -v error -select_streams v:0 -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1 "$e")																		
output_duration=$(bc <<< "$input_duration"-"$cut_duration")																		
ffmpeg -i "$e" -map 0 -c copy -t "$output_duration" output/"$e"																		
done																		
 
 
for g in output/*.mp4;																		
do																		
ffmpeg -i "$g" -ss 00:00:30.000 -vframes 1 "${g%.*}.jpg"																		
done
 
 
 