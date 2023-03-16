import os
import cv2 as cv

#영상 파일 가져오기
path = './data/'
file_name = 'LOLback.mp4' #영상 파일 이름 지정

path_capture = './capture/'
files_list  = os.listdir(path_capture) 
captured_list = [file for file in files_list if file.endswith('.png')]

if captured_list:
    img_index = int(captured_list[-1][8:-4]) + 1
else:
    img_index = 1

video_file = path + file_name
video = cv.VideoCapture(video_file)

fps = video.get(cv.CAP_PROP_FPS)
wait_msec = int(1/fps*1000)
frame_total = int(video.get(cv.CAP_PROP_FRAME_COUNT))

#프레임 이동 조정
frame_table = [1, 5, 10, 20, 30, 50, 100]
frame_index = 2

video_run = True

# 에디터를 실행 여부
edit_iamge = None

if video.isOpened():
    while video_run:
        valid, img = video.read()
        if not valid:
            break
        
        frame_shift = frame_table[frame_index]
        #
        cap = img.copy()
        
        frame = int(video.get(cv.CAP_PROP_POS_FRAMES))
        info = f'Frame: {frame}/{frame_total}, Frame Shift: {frame_shift}'
        cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 0))
        cv.namedWindow('Video Player', cv.WINDOW_NORMAL)
        cv.imshow('Video Player', img)
        
        key = cv.waitKeyEx(wait_msec)
        
        if key in (32, 0x270000, 0x250000, 99, 67): #space, 방향키(우, 좌), c키, C키
            if key == 0x270000:
                video.set(cv.CAP_PROP_POS_FRAMES, frame + frame_shift - 1)
            elif key == 0x250000:
                video.set(cv.CAP_PROP_POS_FRAMES, max(frame - frame_shift - 1,0))
            elif key in (99, 67):
                video.set(cv.CAP_PROP_POS_FRAMES, frame - 1)
                cv.imwrite('capture/captured' + str(img_index).zfill(3) + '.png',cap)
                img_index += 1
            else:
                pass
                
            valid, img = video.read()
            if not valid:
                break
            
            cap = img.copy()
            
            frame = int(video.get(cv.CAP_PROP_POS_FRAMES))
            info = f'Frame: {frame}/{frame_total}, Shift: {frame_shift}'
            cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 0))
            cv.namedWindow('Video Player', cv.WINDOW_NORMAL)
            cv.imshow('Video Player', img)
            
            while True:
                valid, img = video.read()
                if not valid:
                    break
                
                cap = img.copy()
                
                frame = int(video.get(cv.CAP_PROP_POS_FRAMES))
                info = f'Frame: {frame}/{frame_total}, Shift: {frame_shift}'
                cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 0))
                cv.namedWindow('Video Player', cv.WINDOW_NORMAL)
                cv.imshow('Video Player', img)
                
                #일시정지
                key = cv.waitKeyEx()
                
                if key == 32:
                    break
                elif key == 27:
                    video_run = False
                    break
                # e키, E키
                elif key in (101, 69):
                    video.set(cv.CAP_PROP_POS_FRAMES, frame - 1)
                    cv.imwrite('capture/captured' + str(img_index).zfill(3) + '.png',cap)
                    img_index += 1
                    
                    edit_image = cap.copy()
                    
                    video_run = False
                    break
                elif key == 0x270000:
                    video.set(cv.CAP_PROP_POS_FRAMES, frame + frame_shift - 1)
                elif key == 0x250000:
                    video.set(cv.CAP_PROP_POS_FRAMES, max(frame - frame_shift - 1,0))
                elif key in (99, 67):
                    video.set(cv.CAP_PROP_POS_FRAMES, frame - 1)
                    cv.imwrite('capture/captured' + str(img_index).zfill(3) + '.png',cap)
                    img_index += 1
                elif key == 0x260000:
                    frame_index = min(frame_index + 1, len(frame_table) - 1)
                    frame_shift = frame_table[frame_index]
                    video.set(cv.CAP_PROP_POS_FRAMES, frame - 1)
                elif key == 0x280000:
                    frame_index = max(frame_index - 1, 0)
                    frame_shift = frame_table[frame_index]
                    video.set(cv.CAP_PROP_POS_FRAMES, frame - 1)
                                
        elif key == 0x260000:
            frame_index = min(frame_index + 1, len(frame_table) - 1)
            frame_shift = frame_table[frame_index]
        elif key == 0x280000:
            frame_index = max(frame_index - 1, 0)
            frame_shift = frame_table[frame_index]
        elif key == 27:
            break
    
    cv.destroyAllWindows

# 에디터를 띄우는 조건
#if edit_image:
    # TODO