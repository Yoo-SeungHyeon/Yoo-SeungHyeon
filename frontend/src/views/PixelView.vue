<template>
    <div class="pixel-window">
      <div class="scanlines"></div>
  
      <div class="chat-wrapper">
        <div class="chat-header">
          <div class="header-decoration"></div>
          <h1 class="header-title">👾 PLAYER: Yoo-SeungHyeon</h1>
          <div class="header-controls">
            <span class="ctrl-btn">_</span>
            <span class="ctrl-btn">□</span>
            <span class="ctrl-btn">×</span>
          </div>
        </div>
  
        <div class="messages-area" ref="messagesArea">
          <div class="messages-container">
            
            <div class="system-message">
              <span>*** SYSTEM READY ***</span>
            </div>
  
            <div
              v-for="(msg, index) in messages"
              :key="index"
              class="message-row"
              :class="{ 'user-row': msg.isUser }"
            >
              <div class="message-content" :class="{ 'user-content': msg.isUser }">
                <div v-if="!msg.isUser" class="avatar-wrapper">
                  <div class="avatar ai-avatar">
                    🤖
                  </div>
                </div>
  
                <div class="message-body" :class="{ 'user-body': msg.isUser }">
                  <div class="pixel-box">
                    <div class="message-text">{{ msg.text }}</div>
                  </div>
                </div>
  
                <div v-if="msg.isUser" class="avatar-wrapper">
                  <div class="avatar user-avatar">
                    😎
                  </div>
                </div>
              </div>
            </div>
  
            <div v-if="isTyping" class="message-row">
              <div class="message-content">
                <div class="avatar-wrapper">
                  <div class="avatar ai-avatar">🤖</div>
                </div>
                <div class="message-body">
                  <div class="pixel-box typing-box">
                    <div class="typing-indicator">
                      <span>■</span>
                      <span>■</span>
                      <span>■</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
  
            <div ref="bottomRef"></div>
          </div>
        </div>
  
        <div class="input-area">
          <div class="input-container">
            <div class="quick-questions">
              <button
                v-for="question in quickQuestions"
                :key="question.id"
                class="pixel-btn quick-btn"
                @click="askQuestion(question.query)"
              >
                {{ question.label }}
              </button>
            </div>
  
            <div class="input-wrapper">
              <span class="prompt-char">></span>
              <textarea
                v-model="inputMessage"
                placeholder="COMMAND..."
                rows="1"
                ref="textareaRef"
                @input="autoResize"
                @keydown="handleKeydown"
              ></textarea>
              <button
                class="send-button pixel-btn"
                :class="{ 'active': inputMessage.trim() }"
                :disabled="!inputMessage.trim()"
                @click="sendMessage"
              >
                SEND
              </button>
            </div>
            <p class="input-hint">PRESS [ENTER] TO START</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, nextTick, onMounted } from 'vue';
  
  // --- State ---
  const inputMessage = ref('');
  const bottomRef = ref(null);
  const messagesArea = ref(null);
  const textareaRef = ref(null);
  const isTyping = ref(false);
  
  const messages = ref([
    { text: 'HELLO WORLD! 포트폴리오 데이터베이스에 접속했습니다. 무엇을 도와드릴까요?', isUser: false },
  ]);
  
  const quickQuestions = [
    { id: 1, label: '📂 개인정보', query: '개인정보에 대해 알려주세요' },
    { id: 2, label: '💾 PROMTREE', query: 'PROMTREE 프로젝트에 대해 알려주세요' },
    { id: 3, label: '🐾 DailyPet', query: 'DailyPet 프로젝트에 대해 알려주세요' },
    { id: 4, label: '💿 CDD', query: 'CDD 프로젝트에 대해 알려주세요' },
  ];
  
  // --- Methods ---
  
  const askQuestion = (query) => {
    inputMessage.value = query;
    sendMessage();
  };
  
  const autoResize = () => {
    const textarea = textareaRef.value;
    if (textarea) {
      textarea.style.height = 'auto';
      textarea.style.height = Math.min(textarea.scrollHeight, 150) + 'px';
    }
  };
  
  const sendMessage = async () => {
    if (!inputMessage.value.trim()) return;
  
    messages.value.push({
      text: inputMessage.value,
      isUser: true
    });
  
    const userText = inputMessage.value;
    inputMessage.value = '';
  
    if (textareaRef.value) {
      textareaRef.value.style.height = 'auto';
    }
  
    scrollToBottom();
    isTyping.value = true;
  
    setTimeout(() => {
      isTyping.value = false;
      messages.value.push({
        text: `[시스템 응답]: "${userText}"에 대한 데이터 로드 중...\n\n이것은 데모 텍스트입니다. 실제 AI 모델 연결이 필요합니다.`,
        isUser: false
      });
      scrollToBottom();
    }, 1000);
  };
  
  const handleKeydown = (e) => {
    if (e.isComposing) return;
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };
  
  const scrollToBottom = async () => {
    await nextTick();
    bottomRef.value?.scrollIntoView({ behavior: 'smooth' });
  };
  
  onMounted(() => {
    textareaRef.value?.focus();
  });
  </script>
  
  <style>
  /* 레트로 폰트 임포트 */
  @import url('https://fonts.googleapis.com/css2?family=DungGeunMo&display=swap');
  </style>
  
  <style scoped>
  /* Color Variables for Theme */
  .pixel-window {
    --bg-color: #2b213a;       /* Deep Purple Background */
    --chat-bg: #e6e6fa;        /* Light Lavender for chat area */
    --primary: #4f46e5;        /* Purple */
    --accent-mint: #00ff9d;    /* Retro Mint */
    --accent-pink: #ff00ff;    /* Hot Pink */
    --accent-yellow: #fff500;  /* Arcade Yellow */
    --text-dark: #1a1a1a;
    --border-color: #000000;
    
    font-family: 'DungGeunMo', monospace; /* Pixel Font */
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: var(--bg-color);
    padding: 10px;
    box-sizing: border-box;
  }
  
  .chat-wrapper {
    width: 100%;
    max-width: 720px;
    height: 100%;
    max-height: 900px;
    display: flex;
    flex-direction: column;
    background-color: #fff;
    border: 4px solid var(--border-color);
    box-shadow: 8px 8px 0 rgba(0,0,0,0.5);
    position: relative;
    z-index: 2;
  }
  
  /* CRT Scanline Effect */
  .scanlines {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(
      to bottom,
      rgba(255,255,255,0),
      rgba(255,255,255,0) 50%,
      rgba(0,0,0,0.1) 50%,
      rgba(0,0,0,0.1)
    );
    background-size: 100% 4px;
    pointer-events: none;
    z-index: 10;
    opacity: 0.3;
  }
  
  /* Header */
  .chat-header {
    padding: 0.8rem;
    background-color: var(--primary);
    border-bottom: 4px solid var(--border-color);
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #fff;
  }
  
  .header-title {
    font-size: 1.2rem;
    margin: 0;
    text-transform: uppercase;
    text-shadow: 2px 2px 0 #000;
    letter-spacing: 1px;
  }
  
  .header-controls {
    display: flex;
    gap: 8px;
  }
  
  .ctrl-btn {
    background: #c0c0c0;
    color: black;
    width: 20px;
    height: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    border: 2px solid black;
    box-shadow: 2px 2px 0 black;
    cursor: pointer;
  }
  
  .ctrl-btn:active {
    transform: translate(2px, 2px);
    box-shadow: none;
  }
  
  /* Messages Area */
  .messages-area {
    flex: 1;
    overflow-y: auto;
    padding: 1rem;
    background-color: var(--chat-bg);
    /* Checker pattern background */
    background-image: 
      linear-gradient(45deg, #dcdcdc 25%, transparent 25%),
      linear-gradient(-45deg, #dcdcdc 25%, transparent 25%),
      linear-gradient(45deg, transparent 75%, #dcdcdc 75%),
      linear-gradient(-45deg, transparent 75%, #dcdcdc 75%);
    background-size: 20px 20px;
    background-position: 0 0, 0 10px, 10px -10px, -10px 0px;
  }
  
  .system-message {
    text-align: center;
    margin-bottom: 2rem;
    color: #666;
    font-size: 0.8rem;
  }
  
  .system-message span {
    background: #fff;
    padding: 4px 8px;
    border: 2px dashed #999;
  }
  
  /* Message Row */
  .message-row {
    margin-bottom: 1.5rem;
  }
  
  .message-row.user-row {
    display: flex;
    justify-content: flex-end;
  }
  
  .message-content {
    display: flex;
    align-items: flex-end;
    gap: 12px;
    max-width: 90%;
  }
  
  .message-content.user-content {
    flex-direction: row;
  }
  
  /* Avatar */
  .avatar {
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    background: #fff;
    border: 3px solid var(--border-color);
    box-shadow: 4px 4px 0 rgba(0,0,0,0.2);
  }
  
  .ai-avatar { background-color: var(--accent-mint); }
  .user-avatar { background-color: var(--accent-pink); }
  
  /* Pixel Box (Speech Bubble) */
  .pixel-box {
    background-color: #fff;
    border: 3px solid var(--border-color);
    padding: 12px 16px;
    position: relative;
    box-shadow: 6px 6px 0 rgba(0,0,0,0.2);
    image-rendering: pixelated;
  }
  
  .user-body .pixel-box {
    background-color: var(--accent-yellow);
    color: var(--text-dark);
  }
  
  .user-body .pixel-box::after {
    content: '';
    position: absolute;
    right: -9px;
    bottom: 10px;
    width: 0;
    height: 0;
    border-top: 10px solid transparent;
    border-bottom: 10px solid transparent;
    border-left: 10px solid var(--border-color);
  }
  
  .message-body:not(.user-body) .pixel-box::before {
    content: '';
    position: absolute;
    left: -9px;
    bottom: 10px;
    width: 0;
    height: 0;
    border-top: 10px solid transparent;
    border-bottom: 10px solid transparent;
    border-right: 10px solid var(--border-color);
  }
  
  .message-text {
    font-size: 1rem;
    line-height: 1.5;
    white-space: pre-wrap;
    word-break: break-word;
  }
  
  /* Typing Indicator */
  .typing-indicator span {
    display: inline-block;
    font-size: 1rem;
    color: var(--text-dark);
    animation: blink 1s infinite;
  }
  .typing-indicator span:nth-child(2) { animation-delay: 0.2s; }
  .typing-indicator span:nth-child(3) { animation-delay: 0.4s; }
  
  @keyframes blink {
    0%, 100% { opacity: 0.2; }
    50% { opacity: 1; }
  }
  
  /* Input Area */
  .input-area {
    background-color: #c0c0c0;
    padding: 1rem;
    border-top: 4px solid var(--border-color);
  }
  
  .input-container {
    max-width: 100%;
    margin: 0 auto;
  }
  
  /* Quick Questions Buttons */
  .quick-questions {
    display: flex;
    flex-wrap: wrap;
    gap: 0.8rem;
    margin-bottom: 1rem;
    justify-content: flex-start;
  }
  
  .pixel-btn {
    font-family: 'DungGeunMo', monospace;
    border: 3px solid var(--border-color);
    background-color: #fff;
    color: var(--text-dark);
    padding: 8px 16px;
    font-size: 0.9rem;
    cursor: pointer;
    box-shadow: 4px 4px 0 var(--border-color);
    transition: transform 0.1s, box-shadow 0.1s;
  }
  
  .pixel-btn:hover {
    transform: translate(-1px, -1px);
    box-shadow: 6px 6px 0 var(--border-color);
  }
  
  .pixel-btn:active {
    transform: translate(4px, 4px);
    box-shadow: 0 0 0 var(--border-color);
  }
  
  .quick-btn {
    background-color: var(--accent-mint);
  }
  
  .quick-btn:nth-child(2n) {
    background-color: var(--accent-pink);
    color: #fff;
  }
  
  /* Input Wrapper */
  .input-wrapper {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px;
    background-color: #000; /* Terminal Black */
    border: 3px solid var(--border-color);
    box-shadow: inset 4px 4px 0 rgba(255,255,255,0.2);
  }
  
  .prompt-char {
    color: var(--accent-mint);
    font-weight: bold;
    font-size: 1.2rem;
    animation: blink 1s step-end infinite;
  }
  
  .input-wrapper textarea {
    flex: 1;
    background: transparent;
    border: none;
    outline: none;
    color: var(--accent-mint); /* Terminal Green Text */
    font-family: 'DungGeunMo', monospace;
    font-size: 1.1rem;
    resize: none;
    line-height: 1.4;
    caret-color: var(--accent-mint);
  }
  
  .input-wrapper textarea::placeholder {
    color: #005533;
  }
  
  .send-button {
    background-color: var(--primary);
    color: #fff;
    font-weight: bold;
    padding: 8px 12px;
    font-size: 1rem;
  }
  
  .send-button:disabled {
    background-color: #555;
    cursor: not-allowed;
    box-shadow: none;
    transform: none;
  }
  
  .input-hint {
    text-align: right;
    font-size: 0.8rem;
    color: #555;
    margin-top: 0.5rem;
    margin-bottom: 0;
  }
  
  /* Scrollbar Customization */
  .messages-area::-webkit-scrollbar {
    width: 16px;
  }
  .messages-area::-webkit-scrollbar-track {
    background: #c0c0c0;
    border-left: 2px solid black;
  }
  .messages-area::-webkit-scrollbar-thumb {
    background-color: var(--primary);
    border: 2px solid black;
    box-shadow: inset -2px -2px 0 rgba(0,0,0,0.3), inset 2px 2px 0 rgba(255,255,255,0.3);
  }
  
  /* Responsive */
  @media (max-width: 768px) {
    .pixel-window {
      padding: 0;
    }
    .chat-wrapper {
      max-height: 100vh;
      border: none;
    }
  }
  </style>