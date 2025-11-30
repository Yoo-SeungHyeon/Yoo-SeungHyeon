<template>
    <v-app-bar color="primary" elevation="1">
      <v-app-bar-title>AI Chatbot</v-app-bar-title>
      <template v-slot:append>
        <v-btn icon="mdi-dots-vertical"></v-btn>
      </template>
    </v-app-bar>
  
    <v-main class="bg-grey-lighten-4">
      <v-container class="fill-height align-start pb-10" fluid>
        <v-row justify="center">
          <v-col cols="12" md="8" lg="6">
            
            <div v-for="(msg, index) in messages" :key="index" class="d-flex mb-4" :class="msg.isUser ? 'justify-end' : 'justify-start'">
              
              <v-avatar v-if="!msg.isUser" color="primary" size="36" class="mr-2">
                <v-icon icon="mdi-robot" color="white"></v-icon>
              </v-avatar>
  
              <v-sheet
                class="pa-3 rounded-lg"
                :color="msg.isUser ? 'primary' : 'white'"
                :theme="msg.isUser ? 'dark' : 'light'"
                elevation="1"
                max-width="80%"
                style="word-break: break-word; white-space: pre-wrap;"
              >
                {{ msg.text }}
              </v-sheet>
            </div>
  
            <div ref="bottomRef"></div>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  
    <v-footer app color="transparent" class="d-flex justify-center pa-2 pb-4" style="z-index: 100;">
      <v-sheet width="100%" max-width="900" color="transparent">
        <v-textarea
          v-model="inputMessage"
          placeholder="무엇이든 물어보세요..."
          variant="outlined"
          bg-color="white"
          auto-grow
          rows="1"
          max-rows="5"
          hide-details
          rounded="xl"
          density="comfortable"
          @keydown.enter="handleEnter"
        >
          <template v-slot:append-inner>
            <v-fade-transition>
              <v-btn
                v-show="inputMessage.trim().length > 0"
                icon="mdi-arrow-up"
                variant="flat"
                color="primary"
                size="small"
                class="align-self-end mb-1"
                @click="sendMessage"
              ></v-btn>
            </v-fade-transition>
          </template>
        </v-textarea>
      </v-sheet>
    </v-footer>
  </template>
  
  <script setup>
  import { ref, nextTick } from 'vue';
  
  // --- 상태 관리 ---
  const inputMessage = ref('');
  const bottomRef = ref(null);
  const messages = ref([
    { text: '안녕하세요! Vue와 Vuetify로 만든 챗봇입니다.', isUser: false },
  ]);
  
  // --- 이벤트 핸들러 ---
  
  // 1. 메시지 전송 로직
  const sendMessage = async () => {
    if (!inputMessage.value.trim()) return;
  
    // 사용자 메시지 추가
    messages.value.push({
      text: inputMessage.value,
      isUser: true
    });
    
    const userText = inputMessage.value;
    inputMessage.value = ''; // 입력창 초기화
    scrollToBottom();
  
    // (Simulated) AI 응답 대기
    setTimeout(() => {
      messages.value.push({
        text: `Echo: ${userText}\n\n이 메시지는 ChatView 컴포넌트 내부에서 처리되었습니다.`,
        isUser: false
      });
      scrollToBottom();
    }, 600);
  };
  
  // 2. 엔터키 처리 (Shift+Enter 줄바꿈, Enter 전송)
  const handleEnter = (e) => {
    // 한글 조합 중(IME)일 때 중복 전송 방지
    if (e.isComposing) return;
  
    // Shift + Enter: 줄바꿈 허용 (기본 동작)
    if (e.shiftKey) return; 
  
    // Enter: 줄바꿈 막고 전송
    e.preventDefault(); 
    sendMessage();
  };
  
  // 3. 스크롤 자동 이동
  const scrollToBottom = async () => {
    await nextTick();
    bottomRef.value?.scrollIntoView({ behavior: 'smooth' });
  };
  </script>