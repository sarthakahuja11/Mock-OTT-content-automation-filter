RECODE 264	

#!/bin/bash																		

for f in *																		
do																		
ffmpeg -i "$f" -crf 24 "converted/${f%.*}.mp4"																		
if [[ "$f" != *.sh ]]; then																		
rm "$f"																		
fi																		
done																		
 
 
 
 