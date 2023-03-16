# Simple Snap📷(SSNAP:쓰냅)

## 프로젝트 설명
OpenCV Python을 활용하여 만든 간단한 동영상 스냅샷 생성기입니다.</br>
1, 5, 10, 20, 30, 50, 100 단위로 섬세하고 자유로운 프레임 이동이 가능하기 때문에 원하는 스냅샷을 손쉽게 획득할 수 있습니다.</br>
또한, 스냅샷 이미지에 간단한 효과를 다양하게 적용하여 각각 다른 이미지로 저장하는 것이 가능합니다.</br>
결과 이미지 예시는 **[sample](https://github.com/NyaNyak/Simple-Snap/tree/master/sample)** 폴더에서 확인할 수 있습니다.

## 프로젝트 실행 방법

- 아래와 같이 필요한 패키지를 설치합니다.
```
pip install opencv-python opencv-contrib-python
```
- 환경이 준비되었다면, **[data](https://github.com/NyaNyak/Simple-Snap/tree/master/data)** 폴더 안에 원하는 영상을 넣습니다.
- **[snapshot_editor.py](https://github.com/NyaNyak/Simple-Snap/blob/master/snapshot_editor.py)** 의 line 6에서 영상 파일 이름을 알맞게 수정합니다.
- 프로그램 조작법은 아래와 같습니다.

  - Video Player 조작법

    | 키         | 기능     | 
    | ------------ | -------- | 
    | `←` | 프레임 앞으로 이동(영상 시작점 방향으로) | 
    | `→` | 프레임 뒤로 이동 | 
    | `↑` | 이동할 프레임 단위 증가 | 
    | `↓` | 이동할 프레임 단위 감소 | 
    | `space` | 영상 일시정지/재생 | 
    | `c`, `C` | 현재 프레임 캡처 | 
    | `e`, `E` | 현재 프레임 캡처 후 Editor 실행 | 
    | `ESC` | 프로그램 종료 | 

  - Editor 조작법
 
    | 키         | 기능     | 
    | ------------ | -------- | 
    | `←`, `→` | 좌우반전 | 
    | `↑`, `↓` | 상하반전 | 
    | `g`, `G` | BGR -> Grayscale | 
    | `h`, `H` | BGR -> HSV | 
    | `r`, `R` | BGR -> RGB | 
    | `l`, `L` | BGR -> LAB | 
    | `n`, `N` | Negative 적용 | 
    | `s`, `S` | 이미지 저장 |
    | `F5` | 적용된 효과 초기화 | 
    | `ESC` | 프로그램 종료 | 
</br>

## 프로젝트 실행 결과 예시

- 프로그램 실행 시 Video Player에서 영상이 재생됩니다.

![image](https://user-images.githubusercontent.com/81071456/225606656-29d836c4-94df-4481-b420-40a1b8055aad.png)

- 상하좌우 방향키로 프레임 단위 조정 및 프레임 이동이 가능합니다.

![image](https://user-images.githubusercontent.com/81071456/225607300-36ba545f-1df6-4af0-a543-c15ac0b5bf0e.png)

- Video Player에서 `c`, `C` 키로 캡처한 이미지는 **[capture](https://github.com/NyaNyak/Simple-Snap/tree/master/capture)** 폴더에 저장됩니다.

![image](https://user-images.githubusercontent.com/81071456/225609586-2baab7fc-b4d1-4949-8f7f-9692a5b0d8a9.png)

- Video Player에서 `e`, `E`키를 누르면 현재 프레임을 capture 폴더에 자동 저장 후, Video Player는 종료되고 Editor가 실행됩니다.

![image](https://user-images.githubusercontent.com/81071456/225610239-2133d7ab-7c3a-4493-8b43-35bd987bde35.png)

- Editor에서는 해당 프레임에 대해 간단한 효과 적용이 가능합니다.

![image](https://user-images.githubusercontent.com/81071456/225610717-69940b68-06b2-458c-8bc2-d0b64e82f8b4.png)
![image](https://user-images.githubusercontent.com/81071456/225610785-3d1e2a7d-05cc-4bb6-9e57-d7c1742eaa63.png)

- Editor 작업 중 `s`, `S` 키를 누르면 현재 적용된 효과 그대로 **[result](https://github.com/NyaNyak/Simple-Snap/tree/master/result)** 폴더에 이미지가 저장됩니다.

![image](https://user-images.githubusercontent.com/81071456/225611512-6baef540-465b-4831-b6eb-3c03fabdf393.png)


## 참조
- https://github.com/mint-lab/cv_tutorial
```
  - intensity_control.py
  - negative_image_and_flip.py
  - video_player+navigation.py
```
