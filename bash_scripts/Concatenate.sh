#https://trac.ffmpeg.org/wiki/Concatenate																		
 
#Concatenate (i, i+1)		

#!/bin/bash																		
 
mkdir output																		
declare -a files=(*.mp4)																		
for (( i = 0; i < ${#files[*]}; ++ i ))																		
do																		
mkfifo temp1 temp2																		
ffmpeg -y -i "${files[$i]}" -c copy -bsf:v h264_mp4toannexb -f mpegts temp1 2> /dev/null & \																		
ffmpeg -y -i "${files[$i+1]}" -c copy -bsf:v h264_mp4toannexb -f mpegts temp2 2> /dev/null & \																		
ffmpeg -f mpegts -i "concat:temp1|temp2" -c copy -bsf:a aac_adtstoasc "output/${files[$i]%.*}.mp4"																		
#ffmpeg -f concat -safe 0 -i <(for f in *.mp4; do echo "file '$PWD/$f'"; done) -c copy output/output.mp4																		
done																		
 
#Suffix	Linux	for file in *; do mv "$file" "$(basename "$file" .mp4)-Mashup_x4.mp4"; done;																		
 
#Suffix	Windows (powershell)	Dir | Rename-Item -NewName { $_.basename + "_Suffix” + $_.extension}																		
 
 
 