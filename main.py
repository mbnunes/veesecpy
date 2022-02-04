import subprocess, os
import multiprocessing, json

# mode
mode = 0o755

def main():        

    with open('config.json') as json_file:
        data = json.load(json_file)

        for value in data["cameras"]:

            if not os.path.isdir(data["root_dir"]+value):            
                os.mkdir(data["root_dir"]+value, mode)       
                
            multiprocessing.Process(target=start_recording, args=(data,value,)).start()               


def start_recording(data, value):            
    recording_dir = data["root_dir"]+value+"/"
        
    subprocess.call(['ffmpeg',
        '-rtsp_transport', 'tcp',        
	    '-i', str(data["cameras"][value]), # input file/stream	    
        '-c:v', 'libx264',
        '-preset', 'fast',
    	'-segment_time', str(data["number_of_seconds"]), # duration of recording in seconds
        '-map', '0',
        '-crf', '35',
    	'-f', 'segment', # split recording in segments
		'-strftime', '1', # needed for timestamp in filename
        '-segment_format', 'mkv',
		recording_dir + '%Y-%m-%d_%H.%M.%S_' + value + '.mkv'])    

main()