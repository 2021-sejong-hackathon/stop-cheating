# 2021 제10회 세종대학교 SW·AI 해커톤 🏆

### 팀명 : 컨닝 멈춰! 🙅🏻‍♀️

### 주제 : 비대면 시험을 위한 AI 시험 감독관

비대면 시험 환경에서 실시간으로 입력되는 영상/음성 정보를 관리하고 부정행위와 연계된 이상을 감지하거나 경고 발생 및 녹화 등을 통해서 시험 감독 보조를 도와주는 시스템을 구현

#### 1. 문제 정의 및 접근
    
길어지는 코로나로 인해 변화된 대학생활. 이로 인해 대두된 문제점 중 비대면 시험의 공정성 문제 해결
    
1) 너무 많은 부정행위 기회
    
    - 개인 시험장소 주변 시각자료 (컨닝페이퍼, 시험용 이외의 전자기기)
        
        ❗ 문제 해결방법 : 시선 감지
        
    - 개인 시험장소 근처의 협동시험의 가능성
        
        ❗ 문제 해결방법 : 음성 분석
        
    - 전자기기로 시험을 위한 사이트 이외의 접근
        
        ❗ 문제 해결방법 : 다른 창 감지 (허용된 웹사이트의 로고 / 네트워크 분석)
        
    
2) 여러 화면을 일일히 확인하지 않아도 되는 간결함과 편리성
    
3) 모든 학생들의 시험 영상 확인. 무거운 용량
    
    ❗ 문제 해결방법 : 브라우저에서 시험화면 공유
    
#### 2. 최종 전략 및 기능
- 영상 데이터 수집
    - 시험 응시자 영상
        - Python | OpenCV 영상 웹스트리밍 서버
        - 웹브라우저를 통해 웹캠 영상 출력 [https://ichi.pro/ko/opencv-mich-flaskleul-sayonghayeo-web-beulaujeoeseo-bidio-seuteuliming-162330575306240](https://ichi.pro/ko/opencv-mich-flaskleul-sayonghayeo-web-beulaujeoeseo-bidio-seuteuliming-162330575306240) | [http://wandlab.com/blog/?p=94](http://wandlab.com/blog/?p=94)
    - 응시자의 시험 화면 영상


1) 시선 감지

    - MediaPipe and TensorFlow.js | Iris landmark tracking
    [https://blog.tensorflow.org/2020/11/iris-landmark-tracking-in-browser-with-MediaPipe-and-TensorFlowJS.html?m=1](https://blog.tensorflow.org/2020/11/iris-landmark-tracking-in-browser-with-MediaPipe-and-TensorFlowJS.html?m=1) | [https://github.com/google/mediapipe](https://github.com/google/mediapipe) | [https://okdy.tistory.com/entry/MediaPipe와-Tensorflowjs로-브라우저에서-홍채인식하기](https://okdy.tistory.com/entry/MediaPipe%EC%99%80-Tensorflowjs%EB%A1%9C-%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80%EC%97%90%EC%84%9C-%ED%99%8D%EC%B1%84%EC%9D%B8%EC%8B%9D%ED%95%98%EA%B8%B0)
    
    - media pipe [https://google.github.io/mediapipe/solutions/iris.html] | (https://google.github.io/mediapipe/solutions/iris.html)  | [https://github.com/NVlabs/few_shot_gaze] | (https://github.com/NVlabs/few_shot_gaze) | [https://arxiv.org/pdf/1905.01941v2.pdf] | (https://arxiv.org/pdf/1905.01941v2.pdf) | [https://brunch.co.kr/@synabreu/93] | (https://brunch.co.kr/@synabreu/93)
    
    - 미디어파이프(MediaPipe)로 AI Web페이지 개발하기 [https://makernambo.com/m/155?category=774191] | (https://makernambo.com/m/155?category=774191)
    
    - eye tracker
    
    - gaze
    
    
2) 다른 창 감지 (로고 / 네트워크 분석) 패킷 캡쳐 브라우저에서 가능? 
    
    - opencv / PyAutoGui edge 검출 [https://youbidan.tistory.com/19] | (https://youbidan.tistory.com/19) | 
    - 이미지 유사도 [https://bkshin.tistory.com/entry/OpenCV-12-이미지-유사도-비교-사람-얼굴과-해골-합성-모션-감지-CCTV] | (https://bkshin.tistory.com/entry/OpenCV-12-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%9C%A0%EC%82%AC%EB%8F%84-%EB%B9%84%EA%B5%90-%EC%82%AC%EB%9E%8C-%EC%96%BC%EA%B5%B4%EA%B3%BC-%ED%95%B4%EA%B3%A8-%ED%95%A9%EC%84%B1-%EB%AA%A8%EC%85%98-%EA%B0%90%EC%A7%80-CCTV) | [https://aroundck.tistory.com/6399] | (https://aroundck.tistory.com/6399)
    - WebRTC [https://ui.toast.com/weekly-pick/ko_20160812] | (https://ui.toast.com/weekly-pick/ko_20160812) | [https://github.com/webrtc/samples] | (https://github.com/webrtc/samples) 
    
    - image detection
    
3) 음성 분석
    
    - JS로 만드는 AI : Tensorflow.js [https://www.youtube.com/watch?v=a9tD69fEX-U] | (https://www.youtube.com/watch?v=a9tD69fEX-U)
    
    
 
 - 참고자료
    - 2020 해커톤 / 시험감독 [https://velog.io/@asas33/후기2020-제9회-세종대학교-SWAI-해커톤] | (https://velog.io/@asas33/%ED%9B%84%EA%B8%B02020-%EC%A0%9C9%ED%9A%8C-%EC%84%B8%EC%A2%85%EB%8C%80%ED%95%99%EA%B5%90-SWAI-%ED%95%B4%EC%BB%A4%ED%86%A4) | [https://github.com/youjeonghan/Test_Supervisor_AI] | (https://github.com/youjeonghan/Test_Supervisor_AI)
    
    - 온라인 시험 부정행위 방지 (빅브라더즈) WebRTC 기반 [https://geun9716.github.io/about/BigBrothers.html] | (https://geun9716.github.io/about/BigBrothers.html)
