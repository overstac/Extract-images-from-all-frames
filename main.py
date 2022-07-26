import cv2

video= cv2.VideoCapture("video.mp4")
print(video.read())             # printeza cate un frame per print

succes, frame= video.read()

count=1
while succes:
    cv2.imwrite(f"images/{count}.jpeg", frame)
    succes, frame= video.read()
    count +=1