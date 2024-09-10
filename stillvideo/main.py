from frame_extract import frame_extract as ef
from dec_to_binary import dec_to_binary as dtb
from hiding import hide_message
from merge import merge


message = input("enter message: ")
binaryMessage = dtb(message)

frame_no = int(input("enter frame: "))
url =  r'assests\videos\example.mp4'

frame = ef(url,  frame_no)

framewData = hide_message(binaryMessage , frame)

merge(frame_no,framewData,url)


