<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&text=Hi!%20I'm%20SeungHyeon&desc=1%20Coffee%20=%201%20Commit&descAlignY=60&fontAlignY=41"/>

<span style="font-size:1.5em;"><b>"☕ 커피를 넣으면 코드가 나옵니다!"</b></span>

</br>
</br>
</br>

## About Me

</br>

통계학과 컴퓨터공학을 복수 전공하여 AI를 공부하고 있는 개발자 유승현입니다. </br>
성능만이 아닌, 자원과 시간을 고려해 문제 해결에 실질적인 도움이 되는 '최적의 AI'를 추구합니다. </br>
팀의 성장을 위해 새로운 기술 학습을 주저하지 않고, 책임감 있게 프로젝트를 완수합니다. </br>

</br>
</br>
</br>
</br>

## Tech Stack

| 기술        | 상세 내용                                         |
|-------------|---------------------------------------------------|
| Python      | 삼성 SW 역량테스트 Pro                            |
| FastAPI     | 비동기 API 설계, 데이터 정합성 검증               |
| Django      | 데이터 관리, 관리자 페이지 커스터마이즈           |
| Yolo        | 온디바이스 실시간 객체 탐지, 타일링 기반 Segmentation, 문서 레이아웃 분석 |
| Pytorch     | Transformer 인코더 구현 및 모델링                 |
| AWS         | 소셜 로그인, S3 Trigger & Presigned UR, Lambda 라우팅 |
| MySQL       | 3차 정규화를 고려한 설계                         |
| Docker      | 캐시 최적화, 멀티스테이지 빌드, docker compose   |

</br>
</br>
</br>

## 수상 내역

</br>
</br>

| 날짜 | 수상명 | 주최 | 비고 |
|:---:|:---:|:---:|:---:|
| **2025.09.29** | 🏆 **우수상(2등)** | 삼성 전자 | SSAFY 13기 특화 프로젝트 |
| **2025.08.26** | 🏆 **우수상(3등)** | 삼성 전자 | SSAFY 13기 공통 프로젝트 |
| **2025.05.30** | 🏆 **성적 우수상(2등)** | 삼성 전자 | SSAFY 13기 |
| **2023.07.20** | 🏆 **참가상(Top 6)** | iM 뱅크 | It's DGB, I'm Challenger 공모전 |

</br>
</br>
</br>
</br>
</br>

## Projects

</br>

### 1. PROMTREE - RAG를 활용한 물성 정보 추출 및 챗봇 프로젝트

<img src="./images/PROMTREE.png" alt="PROMTREE" width="600" />

|              | 내용                                                                                 |
|:------------:|:-------------------------------------------------------------------------------------|
| **프로젝트 명** | PROMTREE                                                                            |
| **기간**        | 2025.10.10 ~ 2025.11.20                                                             |
| **팀원**        | 6명                                                                                 |

</br>

**프로젝트 소개**  
삼성전자 생산기술연구소의 물성 예측 모델 개발 과정에서, 대용량 데이터셋 확보와 정확한 데이터 파이프라인 구축이 필요하였습니다.</br>
원천 PDF 데이터로부터 물성 정보를 추출하고, 물성 엔지니어가 쉽고 빠르게 접근 가능한 챗봇 서비스를 제공하는 것이 목표였습니다.</br>

</br>

**주요 기능**  
• PDF → Markdown 변환 Parser 개발  
• Markdown에서 정보 추출하는 Extract RAG 구현  
• 물성 데이터검색 및 질의응답 챗봇 서비스 제공  

</br>

**담당 역할 (AI, Backend)**  
• 자체 Parser 개발 및 적용  
• PDF → 물질 정보 추출 데이터 파이프라인 구축  
• FastAPI 기반 챗봇 백엔드 설계/구현  
• Qdrant 벡터 DB로 임베딩 및 검색 시스템 구축  

</br>

**성과**  
• 삼성전자 생산기술연구소 사내 알파테스트에 실제 활용됨  

</br>

**성장 경험**  
• ISO32000 기반 PDF 구조/커스텀 Parser 설계 경험  
• 다양한 RAG 및 벡터DB 실무 적용과 분석 경험  

---

### 2. DAILYPET - 펫 건강 이상 탐지 및 펫 금융상품 추천 서비스

<img src="./images/DAILYPET.png" alt="DAILYPET" width="600" />


|              | 내용                                                                                 |
|:------------:|:-------------------------------------------------------------------------------------|
| **프로젝트 명** | DAILYPET                                                                             |
| **기간**        | 2025.09.01 ~ 2025.09.28                                                             |
| **팀원**        | 6명                                                                                 |

</br>

**프로젝트 소개**  
복잡하고 애매한 펫 보험 및 금융상품 선택 과정과, 반려동물의 건강 문제 조기 인지 어려움을 AI와 데이터로 해결하고자 시작한 프로젝트입니다.

</br>

**주요 기능**  
• 모바일/웨어러블로 일상 데이터 기록  
• 식사·산책 등 데이터 기반 건강 이상 탐지  
• 기록 데이터를 활용한 맞춤 펫 금융상품 추천  

</br>

**담당 역할 (AI, Infra, PM)**  
• 이상치 탐지 AI 모델 개발  
• RAG 기반 데이터 추출 기능 개발  
• 금융상품 추천 모델 개발  
• 인프라: 설계, 배포, CI/CD, IaC, 모니터링 구축  
• 관리자 페이지 개발  

</br>

**성과**  
• SSAFY 특화 프로젝트 우수상 (2등) 수상  

</br>

**성장 경험**  
• 이상치 탐지 모델 설계/구현 경험  
• 추천 시스템 및 필터링 기반 RAG 기법 실습  

---

### 3. CDD(Crack Detection Drone) - 균열 감지 드론 프로젝트

<img src="./images/CDD.png" alt="CDD" width="600" />

|              | 내용                                                                                 |
|:------------:|:-------------------------------------------------------------------------------------|
| **프로젝트 명** | CDD (Crack Detection Drone)                                                        |
| **기간**        | 2025.07.14 ~ 2025.08.17                                                             |
| **팀원**        | 6명                                                                                 |

</br>

**프로젝트 소개**  
고층 건물, 교량 하부 등 관리가 어려운 대형 구조물의 비용/안전문제를 드론과 온디바이스 AI로 해소하여 정밀 모니터링 및 사고 예방을 목표로 수행한 프로젝트입니다.

</br>

**주요 기능**  
• RTSP/MJPEG 기반 드론 영상 실시간 송수신  
• 온디바이스 AI로 실시간 균열 감지  
• LiDAR, Segmentation 모델 활용 정밀 탐지  
• 녹화 영상 → 현장 3D 렌더링  
• 작업자/관리자 웹 공유 페이지  

</br>

**담당 역할 (AI, Infra, Embedded)**  
• Yolo 모델을 활용한 실시간 균열 감지 모델 개발  
• LiDAR 기반 균열 깊이 측정 기능 개발  
• 실시간 영상 송출 기능 개발  
• AWS 인프라 설계 및 구축  

</br>

**성과**  
• SSAFY 공통 프로젝트 우수상 (3등) 수상  

</br>

**성장 경험**  
• 임베디드 환경 및 비디오 송수신/통신 프로토콜 이해  

</br>

**GitHub**  
https://github.com/SSAFY-CDD


</br>
</br>
</br>

<span style="font-size:2em; font-weight:bold;">★ CONTACT ★</span>

<div style="border: 1px solid #333; padding: 20px; margin: 20px auto; max-width: 600px; text-align: left;">

<div style="text-align:center;">
    <span>
        <b>Email</b> : effort-result@naver.com 
        <button 
            onclick="navigator.clipboard.writeText('effort-result@naver.com')" 
            style="
                margin-left:12px; 
                padding:6px 16px; 
                font-size:1em; 
                cursor:pointer; 
                border-radius: 18px; 
                background: linear-gradient(90deg, #3B82F6 0%, #2563EB 100%);
                color: #fff; 
                border: none; 
                transition: background 0.2s, transform 0.2s, box-shadow 0.2s;
                box-shadow: 0 2px 8px rgba(30,58,138,0.08);
            "
            onmouseover="this.style.background='linear-gradient(90deg, #2563EB 0%, #3B82F6 100%)'; this.style.transform='translateY(-2px)'; this.style.boxShadow='0 6px 20px rgba(30,58,138,0.15)';"
            onmouseout="this.style.background='linear-gradient(90deg, #3B82F6 0%, #2563EB 100%)'; this.style.transform='none'; this.style.boxShadow='0 2px 8px rgba(30,58,138,0.08)';"
        >이메일 복사</button>
    </span>
</div>

</div>

</br>
</br>
</br>

## GitHub Stats

  <img src="https://github-readme-stats.vercel.app/api?username=Yoo-SeungHyeon&show_icons=true&theme=transparent&title_color=1E3A8A&text_color=334155&icon_color=3B82F6&ring_color=3B82F6" alt="GitHub Stats"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Yoo-SeungHyeon&layout=compact&theme=transparent&title_color=1E3A8A&text_color=334155" alt="Top Languages"/>
  
  <br/>
  
  <img src="https://streak-stats.demolab.com?user=Yoo-SeungHyeon&theme=transparent&hide_border=true&ring=3B82F6&fire=EF4444&currStreakLabel=3B82F6" alt="GitHub Streak"/>
  
  <br/><br/>
  
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=Yoo-SeungHyeon&bg_color=ffffff00&color=1E3A8A&line=3B82F6&point=1E3A8A&area=true&hide_border=true" alt="Activity Graph"/>
  

</br>
</br>
</br>

</div>
