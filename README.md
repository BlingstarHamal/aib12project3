# aib12project3


## 데이터 설명

prototype 폴더 내부
base_data1~basedata3.csv 원본 데이터 파일

eda.ipynb 로 3개의 데이터파일을 data.csv로 합쳐주었습니다

uploadcsv.ipynb를 통해 로컬 posgresql에 업로드 하였습니다.

light_gbm.ipynb 로 머신머닝 모델링을 진행하였고 knn_model.pkl파일이 형성됩니다.

__init__.py 와 templates/index.html 로 flask를 진행하였습니다. app_start.py를 실행하면 진행됩니다.


# 당뇨병 진단 서비스  

## 과정

![무제](https://user-images.githubusercontent.com/97571812/172056398-b8e383de-d28c-4063-8c94-b9f215dcd874.png)  

## 데이터 수집  
국립보건연구원에서 진행하는 한국인 유전체 역학 조사 사업 코호트에서 제공하는 자료 (http://www.cdc.go.kr/contents.es?mid=a40504070100)  
병력 가족력 생활습관 임상자료 포함

## 전처리
SAS을 CSV 파일로 전환 (https://dumbmatter.com/sas7bdat/)  
9천 여개의 행  
PostgresSQL 로컬 데이터 베이스 형성  

## 머신 러닝
PostgresSQL에서 데이터 불러오기  
Light GBM 모델링  
Joblib 이용 pkl 추출  

## 웹 개발 및 배포  
Flask를 이용하여 21개의 항목을 입력하면 당뇨병 진단 가능성을 예상하는 웹 어플리케이션을 개발  
Heroku를 통해 배포 (https://pj3hamal.herokuapp.com/)  

## 한계 및 보완 계획  
데이터 양에 비해 적은 당뇨병 진단자 수  
배경지식 부족으로 임상데이터를 이용치 못함  
CSS 습득후 웹 어플리케이션 업데이트 필요
