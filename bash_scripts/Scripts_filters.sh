
Speed Up	 Windows	for %f in ("*.mp4") do ( ffmpeg -i "%~f" -filter_complex "[0:v]setpts=0.67*PTS[v];[0:a]atempo=1.5[a]" -map "[v]" -map "[a]" "output\%~f")																		
 
Thumbnail	 Windows	for %f in ("*.mp4") do (ffmpeg.exe -i "%~f" -ss 00:00:10.000 -vframes 1 "%~f.png")																		
 
Check Formats	 Linux	youtube-dl -F 'http://www.xyzabc.com/some-alphanumeric-string'																		
 
Download Channel Linux	youtube-dl -f 22 -ciw -o "ytDownload/%(title)s.%(ext)s" -v <url-of-channel>																		
 
		 youtube-dl --match-filter "duration < 301" -ciw -o "ytDownload/%(title)s.%(ext)s" -v '<channel_url>'																		
 
Conversion Best	 ffmpeg -i input.mp4 -vcodec libx265 -crf 24 output.mp4																		
 
		  -o '%Home%\ytDownload\%(title)s.%(ext)s'																		
 
Image Overlay	 Windows	for %f in ("*.mp4") do ( ffmpeg -i "%~f" -i logo.png -filter_complex "[0:v][1:v] overlay=72:H-h-60:" -pix_fmt yuv420p -c:a copy "output\%~f")	449.7751124																				
		 youtube-dl --extract-audio --match-filter "duration < 301" -o "%(title)s.%(ext)s" <url to playlist> 																		
 
Checking extension		if [[ "$f" == *.mp4 ]]; then																		
 
Check length of video		duration=$(ffprobe -v quiet -of csv=p=0 -show_entries format=duration "$f")																		
		                for f in *.mp4;  
                                do  duration=$(ffprobe -v quiet -of csv=p=0 -show_entries format=duration "$f");   
                                duration1=${duration%.*};   
                                echo "$duration1" " - " "$f" >> durations.txt; 
                                done	

