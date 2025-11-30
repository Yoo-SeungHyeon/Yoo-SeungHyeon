<template>
  <v-container class="py-8 py-md-12" fluid>
    <v-row justify="center">
      <v-col cols="12" lg="10" xl="8">

        <!-- Hero Section -->
        <v-card class="mb-8 overflow-hidden" variant="flat" color="grey-darken-4">
          <v-row no-gutters>
            <v-col cols="12" md="6" class="d-flex flex-column justify-center pa-8 pa-md-12">
              <div class="text-overline text-grey-lighten-1 mb-2 tracking-wide">AI & Data Pipeline</div>
              <h1 class="text-h3 text-md-h2 font-weight-bold text-white mb-4">PROMTREE</h1>
              <p class="text-body-1 text-grey-lighten-2 mb-6">
                RAG를 활용한 물성 정보 추출 및 챗봇 프로젝트
              </p>
              <div class="d-flex flex-wrap ga-2">
                <v-chip variant="outlined" color="white" size="small">FastAPI</v-chip>
                <v-chip variant="outlined" color="white" size="small">Qdrant</v-chip>
                <v-chip variant="outlined" color="white" size="small">RAG</v-chip>
                <v-chip variant="outlined" color="white" size="small">LLM</v-chip>
              </div>
            </v-col>
            <v-col cols="12" md="6">
              <v-img
                src="/images/PROMTREE.png"
                height="100%"
                min-height="280"
                cover
              ></v-img>
            </v-col>
          </v-row>
        </v-card>

        <!-- Project Meta -->
        <v-row class="mb-8">
          <v-col v-for="meta in projectMeta" :key="meta.label" cols="6" md="3">
            <div class="text-caption text-grey-darken-1 text-uppercase tracking-wide mb-1">{{ meta.label }}</div>
            <div class="text-body-1 font-weight-medium">{{ meta.value }}</div>
          </v-col>
        </v-row>

        <v-divider class="mb-10"></v-divider>

        <!-- Overview Section -->
        <section class="mb-12">
          <h2 class="section-title">Overview</h2>
          <v-row>
            <v-col cols="12" md="8">
              <p class="text-body-1 text-grey-darken-2 mb-4" style="line-height: 1.8;">
                삼성전자 생산기술연구소의 물성 예측 모델 개발 과정에서, 대용량 데이터셋 확보와
                정확한 데이터 파이프라인 구축이 필요하였습니다.
              </p>
              <p class="text-body-1 text-grey-darken-2" style="line-height: 1.8;">
                본 프로젝트는 원천 PDF 데이터로부터 물성 정보를 추출하고,
                물성 엔지니어가 쉽고 빠르게 접근 가능한 <strong>챗봇 서비스를 제공</strong>하는 것을 목표로 하였습니다.
              </p>
            </v-col>
          </v-row>
        </section>

        <!-- Tech Stack Section -->
        <section class="mb-12">
          <h2 class="section-title">Tech Stack</h2>
          <div class="d-flex flex-wrap ga-2">
            <v-chip v-for="tech in techStack" :key="tech" variant="outlined" size="default" class="font-weight-medium">
              {{ tech }}
            </v-chip>
          </div>
        </section>

        <!-- Key Features Section -->
        <section class="mb-12">
          <h2 class="section-title">Key Features</h2>
          <v-row>
            <v-col v-for="(feature, i) in features" :key="i" cols="12" md="4">
              <v-card variant="outlined" class="pa-6 h-100 feature-card">
                <div class="text-h4 font-weight-bold text-grey-lighten-1 mb-4">{{ String(i + 1).padStart(2, '0') }}</div>
                <p class="text-body-1 text-grey-darken-3">{{ feature }}</p>
              </v-card>
            </v-col>
          </v-row>
        </section>

        <!-- My Role Section -->
        <section class="mb-12">
          <h2 class="section-title">My Contributions</h2>
          <v-row>
            <v-col cols="12" md="8">
              <div class="role-list">
                <div v-for="(role, i) in roles" :key="i" class="role-item d-flex align-start mb-5">
                  <div class="role-number text-grey-darken-1 font-weight-medium mr-4">{{ String(i + 1).padStart(2, '0') }}</div>
                  <div>
                    <p class="text-body-1 text-grey-darken-3">{{ role }}</p>
                  </div>
                </div>
              </div>
            </v-col>
          </v-row>
        </section>

        <v-divider class="mb-10"></v-divider>

        <!-- Results Section -->
        <section class="mb-12">
          <h2 class="section-title">Results</h2>
          <v-row class="mb-10">
            <v-col cols="12" md="8">
              <p class="text-body-1 text-grey-darken-2" style="line-height: 1.8;">
                삼성전자 생산기술연구소 사내 알파테스트에 실제 활용됨
              </p>
            </v-col>
          </v-row>

          <h2 class="section-title">Learnings</h2>
          <v-row>
            <v-col cols="12" md="8">
              <div class="learning-list">
                <div v-for="(learning, i) in learnings" :key="i" class="d-flex align-start mb-5">
                  <div class="text-grey-darken-1 font-weight-medium mr-4" style="min-width: 24px;">{{ String(i + 1).padStart(2, '0') }}</div>
                  <p class="text-body-1 text-grey-darken-3">{{ learning }}</p>
                </div>
              </div>
            </v-col>
          </v-row>
        </section>

      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
const projectMeta = [
  { label: 'Duration', value: '2025.10 - 2025.11' },
  { label: 'Team Size', value: '6명' },
  { label: 'Role', value: 'AI & Backend Lead' },
  { label: 'Client', value: '삼성전자' }
];

const features = [
  'PDF → Markdown 변환 Parser 자체 개발',
  'Markdown 구조에서 정확한 정보 추출을 위한 Extract RAG 구현',
  '물성 데이터 검색 및 질의응답 챗봇 서비스 제공'
];

const roles = [
  '자체 PDF Parser 개발 및 데이터 파이프라인 구축',
  'FastAPI 기반 챗봇 백엔드 API 설계 및 구현',
  'Qdrant 벡터 DB를 활용한 임베딩 및 검색 시스템 최적화',
  'LLM 응답 품질 향상을 위한 프롬프트 엔지니어링'
];

const learnings = [
  'ISO32000 기반 PDF 구조 분석 및 커스텀 Parser 설계 경험',
  '다양한 RAG 파이프라인 구성 및 벡터 DB(Qdrant) 실무 적용 경험'
];

const techStack = ['Python', 'FastAPI', 'Qdrant', 'LangChain', 'OpenAI API', 'Docker'];
</script>

<style scoped>
.tracking-wide {
  letter-spacing: 0.1em;
}

.section-title {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: #9e9e9e;
  margin-bottom: 1.5rem;
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
