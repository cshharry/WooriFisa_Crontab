# WooriFISA 미니프로젝트 : 


<br/>

<details>
  <summary>목차</summary>  
  
  - [수행 과제](#notebook-수행-과제)
  - [팀원](#raising_hand-팀원)
  - [실습환경](#실습환경)
  - [시각화](#bar_chart-시각화)
  - [트러블슈팅](#hammer-트러블슈팅)
  - [회고](#thought_balloon-회고)
      
</details>

## :notebook: 수행 과제
- Faker 라이브러리 데이터 자동 생성
- Crontab 자동삭제
- 사용자 데이터 분석 및 시각화

<br/>

## :raising_hand: 팀원
|<img src="" width="80">|<img src="" width="80">|<img src="" width="80">|<img src="https://github.com/cshharry.png" width="80">|
|:---:|:---:|:---:|:---:|
|[강유완]()|[안재형]()|[이정욱]()|[조성현](https://github.com/cshharry)|

<br/>

## 실습환경
:penguin: **Ubuntu server 22.04.4 LTS**
:book: **ELK Stack 7.11.1**

<br/>

## 가짜 데이터 생성
![image](https://github.com/user-attachments/assets/fb2112e5-4a42-4ec0-be21-2936daf5d4b3)

#### 실행 코드
```
python3 generate_fake_data_periodically.py
```
#### fake_data.csv 파일 생성
![image](https://github.com/user-attachments/assets/819e5fcb-e20f-4e52-8de0-acba9d707e74)

#### crontab을 사용하여 1분마다 csv 파일 삭제
![image](https://github.com/user-attachments/assets/ad4d7a42-fb13-42e5-bbad-aa1a48717d12)

#### crontab 설정
```
* * * * * rm /home/username/fake_data.csv
```        
## :bar_chart: 시각화
<p align="center">
  <img width="70%" src="">
</p>

<br/>

## :hammer: 트러블슈팅
### 1
- 

<br/>

## :thought_balloon: 회고
### 강유완
> 
<br/>

### 안재형
> 
<br/>

### 이정욱
> 
<br/>

### 조성현
> 
<br/>
