import os
import cv2 as cv
import numpy as np

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
is_edit = False
edit_image = None

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
        
        if key in (32, 0x270000, 0x250000, 99, 67, 101, 69): #space, 방향키(우, 좌), c키, C키, e키 E키
            if key == 0x270000: # 오른쪽 방향키 : 프레임 뒤로 이동
                video.set(cv.CAP_PROP_POS_FRAMES, frame + frame_shift - 1)
            elif key == 0x250000: # 왼쪽 방향키 : 프레임 앞으로 이동(영상 시작점 쪽으로)
                video.set(cv.CAP_PROP_POS_FRAMES, max(frame - frame_shift - 1,0))
            elif key in (99, 67): # c키, C키 : 현재 프레임 캡처
                video.set(cv.CAP_PROP_POS_FRAMES, frame - 1)
                cv.imwrite('capture/captured' + str(img_index).zfill(3) + '.png',cap)
                img_index += 1
            elif key in (101, 69): # e키, E키 : 현재 프레임 캡처 후 에디터 열기
                video.set(cv.CAP_PROP_POS_FRAMES, frame - 1)
                cv.imwrite('capture/captured' + str(img_index).zfill(3) + '.png',cap)
                    
                is_edit = True
                edit_image = 'capture/captured' + str(img_index).zfill(3) + '.png'
                    
                img_index += 1                    
                video_run = False
                cv.destroyWindow('Video Player')
                break
                
            else:
                pass
                
            valid, img = video.read()
            if not valid:
                break
            
            cap = img.copy()
            
            frame = int(video.get(cv.CAP_PROP_POS_FRAMES))
            info = f'Frame: {frame}/{frame_total}, Frame Shift: {frame_shift}'
            cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 0))
            cv.namedWindow('Video Player', cv.WINDOW_NORMAL)
            cv.imshow('Video Player', img)
            
            while True:
                valid, img = video.read()
                if not valid:
                    break
                
                cap = img.copy()
                
                frame = int(video.get(cv.CAP_PROP_POS_FRAMES))
                info = f'Frame: {frame}/{frame_total}, Frame Shift: {frame_shift}'
                cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 0))
                cv.namedWindow('Video Player', cv.WINDOW_NORMAL)
                cv.imshow('Video Player', img)
                
                #일시정지
                key = cv.waitKeyEx()
                
                if key == 32: # 스페이스바 : 영상 일시정지, 재생
                    break
                elif key == 27: # esc키 : 프로그램 종료
                    video_run = False
                    break
                elif key in (101, 69): 
                    video.set(cv.CAP_PROP_POS_FRAMES, frame - 1)
                    cv.imwrite('capture/captured' + str(img_index).zfill(3) + '.png',cap)
                    
                    is_edit = True
                    edit_image = 'capture/captured' + str(img_index).zfill(3) + '.png'
                    
                    img_index += 1
                    video_run = False
                    cv.destroyWindow('Video Player')
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
                                
        elif key == 0x260000: # 위 방향키 : 
            frame_index = min(frame_index + 1, len(frame_table) - 1)
            frame_shift = frame_table[frame_index]
        elif key == 0x280000:
            frame_index = max(frame_index - 1, 0)
            frame_shift = frame_table[frame_index]
        elif key == 27:
            break
    
    cv.destroyAllWindows

# 에디터 띄우기
if is_edit:
    img = cv.imread(edit_image)
    img2 = img
    
    path_edited = './result/'
    files  = os.listdir(path_edited) 
    edited_list = [file for file in files if file.endswith('.png')]

    if edited_list:
        result_index = int(edited_list[-1][8:-4]) + 1
    else:
        result_index = 1
        
    is_Gray = False
    is_HSV = False
    is_RGB = False
    is_LAB = False
    
    if img is not None:
        while True:
            cv.namedWindow('Editor', cv.WINDOW_NORMAL)
            cv.imshow('Editor', img)
            
            # 키 이벤트
            key = cv.waitKeyEx(10)
            if key == 27: # ESC키 : 프로그램 종료
                break
            elif key in (103, 71): # g키, G키 : grayscale
                if is_Gray:
                    pass
                else:
                    img = img2
                    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                    is_Gray = True
                    is_HSV = False
                    is_RGB = False
                    is_LAB = False
            elif key in (104, 72): # h키, H키 : BGR -> HSV
                if is_HSV:
                    pass
                else:
                    img = img2
                    img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
                    is_HSV = True
                    is_Gray = False
                    is_RGB = False
                    is_LAB = False
            elif key in (114, 82): # r키, R키 : BGR -> RGB
                if is_RGB:
                   pass
                else:
                    img = img2
                    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
                    is_RGB = True
                    is_Gray = False
                    is_HSV = False
                    is_LAB = False
            elif key in (108, 76): # l키, L키 : BGR -> LAB
                if is_LAB:
                    pass
                else:
                    img = img2
                    img = cv.cvtColor(img, cv.COLOR_BGR2LAB)
                    is_LAB = True
                    is_Gray = False
                    is_HSV = False
                    is_RGB = False
            elif key in (0x270000, 0x250000): # 좌, 우 방향키 : 좌우반전
                img = cv.flip(img, 1)
            elif key in (0x260000, 0x280000): # 상, 하 방향키 : 상하반전
                img = cv.flip(img, 0)
            elif key in (110, 78): # n키, N키 : 보색
                img = cv.bitwise_not(img)
            elif key == 0x740000: # F5키 : 편집 초기화(캡처 원본 이미지로 돌아가기)
                img = img2
                is_Gray = False
                is_HSV = False
                is_RGB = False
                is_LAB = False
            elif key in (115, 83): # s키, S키 : 편집한 이미지 저장
                cv.imwrite('result/edited' + str(result_index).zfill(3) + '.png',img)
                result_index += 1

        cv.destroyAllWindows()