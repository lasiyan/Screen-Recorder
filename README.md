# Screen-Recorder

screen recorder using python and openCV

본 프로젝트는 파이썬 환경에서 openCV를 활용한 화면 녹화 기능을 구현한다.

## 개발 환경

* OS : Windows 10 Pro 64bit
* CPU : AMD Ryzen 5 3600 6-Core Processor 3.59 GHz
* RAM : 16.00GB
* IDE : Microsoft Visual Studio Code
* Version : Python 3.8.5

## 사용 기술

Python, Tkinter, OpenCV API

## 부가 설명

 먼저 영역 설정을 위해 main.py에 Tkinter를 활용하여 UI를 구현한다.
그리고 Keyboard 모듈을 활용하여 Alt+1 부터 Alt+3까지 각각 다른 기능을 수행하도록 이벤트를 분기시키고,
다이얼로그를 Resize하여 녹화하고자 하는 영역을 설정한다.

이후 func.py부분에 Record 및 Screenshot 관련 함수를 구현하였으며, 레코딩 사이즈에 따라 Frame rate가 변화되는 점을 고려하여,
최초 10회에 해당하는 FPS를 구하고 해당 값을 기반으로 MP4G 영상을 생성, 녹화를 진행한다.

녹화 간 Dialog가 함께 녹화되는 것을 방지하기 위해 alpha 값을 0.0으로 변경하여 투명화시키고, 녹화가 종료되는 시점에 복원한다.
저장할 파일은 time모듈을 사용하여 시간별로 구분한다.

## 실행 과정

1. 소스코드 Set-up
2. 실행 후 녹화/캡처를 진행할 영역 설정
3. Alt+1로 녹화 진행 및 Alt+2로 녹화 종료 또는 Alt+3으로 스크린 캡처 진행

## 실행 결과

[![Demo Doccou alpha](https://j.gifs.com/Y7yN7O.gif)](https://youtu.be/R-E4UvOoK0E)

