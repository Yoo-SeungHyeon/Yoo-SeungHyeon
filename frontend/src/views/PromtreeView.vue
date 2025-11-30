<template>
  <v-container class="py-8 py-md-12" fluid>
    <v-row justify="center">
      <v-col cols="12" md="10" lg="9" xl="8">

        <!-- Header -->
        <div class="text-center mb-10">
          <h1 class="text-h3 text-md-h2 font-weight-bold">PROMTREE</h1>
        </div>

        <!-- Section 1: Image + 프로젝트 소개 -->
        <v-row class="mb-10">
          <v-col cols="12" md="6">
            <v-img
              src="/images/PROMTREE.png"
              class="rounded-lg"
              :aspect-ratio="16/10"
              cover
            ></v-img>
          </v-col>
          <v-col cols="12" md="6">
            <h2 class="text-h5 text-md-h4 font-weight-bold mb-5">
              RAG를 활용한 물성 정보 추출 및 챗봇
            </h2>
            <h3 class="info-section-title">프로젝트 소개</h3>
            <table class="info-table">
              <tr>
                <td class="info-label">프로젝트 명</td>
                <td class="info-value">PROMTREE</td>
              </tr>
              <tr>
                <td class="info-label">목표</td>
                <td class="info-value">RAG 기법을 활용해 PDF에서 물성 정보 추출, 챗봇 형태로 데이터 접근</td>
              </tr>
              <tr>
                <td class="info-label">기간</td>
                <td class="info-value">2025.10.10 ~ 2025.11.20</td>
              </tr>
              <tr>
                <td class="info-label">팀원</td>
                <td class="info-value">6명</td>
              </tr>
            </table>
          </v-col>
        </v-row>

        <!-- Section 2: 프로젝트 배경 + Tech Stack -->
        <v-row class="mb-10">
          <v-col cols="12" md="6">
            <h3 class="info-section-title">프로젝트 배경</h3>
            <p class="text-body-1 text-grey-darken-2" style="line-height: 1.9;">
              삼성전자 생산기술 연구소에서 물성 예측 모델 개발을 위해서 <strong>대용량의 데이터셋</strong>이
              필요했습니다. 그래서 <strong>원천 자료(PDF)</strong>에서 필요한 정보만 정확하게 가져오는
              서비스가 필요했고, 추가로 물성 엔지니어가 편하게 <strong>물성 정보를 찾을 수 있게</strong> 이를
              도와주는 <strong>챗봇 서비스</strong> 또한 필요하여 이를 해결하고자 프로젝트를 시작하였습니다.
            </p>
          </v-col>
          <v-col cols="12" md="6">
            <h3 class="info-section-title">Tech Stack</h3>
            <div class="d-flex flex-wrap ga-2">
              <v-chip v-for="tech in techStack" :key="tech" variant="outlined" size="small" class="font-weight-medium">
                {{ tech }}
              </v-chip>
            </div>
          </v-col>
        </v-row>

        <v-divider class="mb-10"></v-divider>

        <!-- Key Features & My Role -->
        <v-row class="mb-12">
          <!-- Left: 주요기능 + 담당역할 -->
          <v-col cols="12" md="5">
            <section class="mb-8">
              <h3 class="info-section-title">주요기능</h3>
              <ol class="text-body-2 text-grey-darken-2 pl-5" style="line-height: 2;">
                <li v-for="feature in features" :key="feature">{{ feature }}</li>
              </ol>
            </section>
            <section>
              <h3 class="info-section-title">담당 역할 (AI, Backend)</h3>
              <ol class="text-body-2 text-grey-darken-2 pl-5" style="line-height: 2;">
                <li v-for="role in roles" :key="role">{{ role }}</li>
              </ol>
            </section>
          </v-col>
          <!-- Right: 기능 다이어그램 -->
          <v-col cols="12" md="7">
            <v-img
              src="/images/PROMTREE_FEATURE.png"
              class="rounded-lg"
              :height="350"
              :aspect-ratio="1"
              contain  
            ></v-img>
          </v-col>
        </v-row>

        <!-- Deep Dive Q&A -->
        <section class="mb-12">
          <h3 class="section-title">Deep Dive</h3>
          <v-row>
            <v-col v-for="(qa, i) in qaItems" :key="i" cols="12" md="6">
              <v-img
                :src="qa.image"
                class="rounded-lg mb-4"
                :aspect-ratio="16/9"
                cover
              ></v-img>
              <p class="text-body-1 font-weight-bold text-grey-darken-4 mb-2">
                Q. {{ qa.question }}
              </p>
              <p class="text-body-2 text-grey-darken-2" style="line-height: 1.8;">
                A. {{ qa.answer }}
              </p>
            </v-col>
          </v-row>
        </section>

        <v-divider class="mb-10"></v-divider>

        <!-- Results & Learnings -->
        <v-row>
          <v-col cols="12" md="5">
            <v-img
              src="/images/PROMTREE_SAMSUNG.jpg"
              class="rounded-lg"
              :aspect-ratio="4/3"
              cover
            ></v-img>
          </v-col>
          <v-col cols="12" md="7">
            <section class="mb-6">
              <h3 class="info-section-title">프로젝트 성과</h3>
              <ul class="text-body-1 text-grey-darken-2 pl-5">
                <li>[삼성전자 생산기술 연구소] 사내 알파 테스트에 활용</li>
              </ul>
            </section>
            <section>
              <h3 class="info-section-title">프로젝트에서 성장한 점</h3>
              <ul class="text-body-2 text-grey-darken-2 pl-5" style="line-height: 2;">
                <li v-for="learning in learnings" :key="learning">{{ learning }}</li>
              </ul>
            </section>
          </v-col>
        </v-row>

      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
const features = [
  'PDF를 마크다운으로 변환하는 Parser',
  '마크다운에서 필요한 정보를 추출하는 Extract RAG',
  '물성 데이터 검색을 위한 챗봇'
];

const qaItems = [
  {
    image: '/images/PROMTREE_PARSER.png',
    question: '시중에 존재하는 Parser가 아닌 자체 Parser를 개발한 이유는?',
    answer: '기존의 Parser는 문서를 그대로 추출하는 것이 목표입니다. 하지만 저희는 사람이 보기에 비슷하게 추출하는 것이 아닌 AI가 데이터를 추출하기 쉬운 형태를 원했기에 표나 이미지를 추가로 전처리하는 자체 Parser를 개발하였습니다.'
  },
  {
    image: '/images/PROMTREE_PIPELINE.png',
    question: '파이프라인 구축에서 가장 힘들었던 부분은?',
    answer: '데이터 추출 정확도 99%라는 목표를 충족하기 위해서는 상대적으로 구조가 정형화된 MSDS에서는 정확도가 100%에 근접해야 했습니다. 이를 위해 정규표현식, FewShot, 앙상블 등 다양한 방법을 시도하면서 95%에서 99%까지 정확도를 올리는 과정이 가장 힘들었던 부분입니다.'
  }
];

const roles = [
  '자체 Parser 개발',
  'PDF에서 물질 정보 추출 파이프라인 구축',
  'FastAPI를 활용한 챗봇 백엔드 구축',
  'Qdrant를 활용한 벡터 저장 및 검색 기능'
];

const learnings = [
  'PDF 표준(ISO 32000)에 대한 이해',
  '다양한 Parser의 장단점',
  'Document Layout Model에 대한 학습',
  '다양한 RAG 기법의 장단점',
  '검색에 사용할 수 있는 다양한 DB에 대한 이해',
  '표 인식 모델에 대한 학습'
];

const techStack = ['Python', 'FastAPI', 'Qdrant', 'LangChain', 'OpenAI API', 'Docker'];
</script>

<style scoped>
.section-title {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #757575;
  margin-bottom: 1rem;
}

.info-section-title {
  font-size: 1rem;
  font-weight: 600;
  color: #212121;
  margin-bottom: 0.75rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid #e0e0e0;
}

.info-table {
  width: 100%;
  border-collapse: collapse;
}

.info-table tr {
  border-bottom: 1px solid #f5f5f5;
}

.info-table tr:last-child {
  border-bottom: none;
}

.info-label {
  width: 100px;
  padding: 0.6rem 0;
  font-size: 0.875rem;
  font-weight: 500;
  color: #757575;
  vertical-align: top;
}

.info-value {
  padding: 0.6rem 0;
  font-size: 0.875rem;
  color: #424242;
  line-height: 1.6;
}

.feature-card {
  border-color: #e0e0e0 !important;
  transition: all 0.2s ease;
}

.feature-card:hover {
  border-color: #212121 !important;
  transform: translateY(-2px);
}

.role-number {
  font-size: 0.875rem;
  min-width: 24px;
}
</style>
