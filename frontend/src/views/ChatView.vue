<template>
  <div class="chat-wrapper">
    <!-- Header -->
    <div class="chat-header">
      <h1 class="header-title">Yoo-SeungHyeon's Portfolio</h1>
    </div>

    <!-- Messages Area -->
    <div class="messages-area" ref="messagesArea">
      <div class="messages-container">

        <!-- Messages -->
        <div
          v-for="(msg, index) in messages"
          :key="index"
          class="message-row"
          :class="{ 'user-row': msg.isUser }"
        >
          <div class="message-content" :class="{ 'user-content': msg.isUser }">
            <!-- AI Avatar -->
            <div v-if="!msg.isUser" class="avatar-wrapper">
              <div class="avatar ai-avatar">
                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="1.5"/>
                  <circle cx="9" cy="10" r="1.5" fill="currentColor"/>
                  <circle cx="15" cy="10" r="1.5" fill="currentColor"/>
                  <path d="M8 15c1.5 2 6.5 2 8 0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                </svg>
              </div>
            </div>

            <!-- Message Text -->
            <div class="message-body" :class="{ 'user-body': msg.isUser }">
              <div class="message-text">{{ msg.text }}</div>
            </div>

            <!-- User Avatar -->
            <div v-if="msg.isUser" class="avatar-wrapper">
              <div class="avatar user-avatar">
                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="12" cy="8" r="4" stroke="currentColor" stroke-width="1.5"/>
                  <path d="M4 20c0-4 4-6 8-6s8 2 8 6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                </svg>
              </div>
            </div>
          </div>
        </div>

        <!-- Typing Indicator -->
        <div v-if="isTyping" class="message-row">
          <div class="message-content">
            <div class="avatar-wrapper">
              <div class="avatar ai-avatar">
                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="1.5"/>
                  <circle cx="9" cy="10" r="1.5" fill="currentColor"/>
                  <circle cx="15" cy="10" r="1.5" fill="currentColor"/>
                  <path d="M8 15c1.5 2 6.5 2 8 0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                </svg>
              </div>
            </div>
            <div class="message-body">
              <div class="typing-indicator">
                <span></span>
                <span></span>
                <span></span>
              </div>
            </div>
          </div>
        </div>

        <div ref="bottomRef"></div>
      </div>
    </div>

    <!-- Input Area -->
    <div class="input-area">
      <div class="input-container">
        <!-- Quick Questions -->
        <div class="quick-questions">
          <button
            v-for="question in quickQuestions"
            :key="question.id"
            class="quick-btn"
            @click="askQuestion(question.query)"
          >
            {{ question.label }}
          </button>
        </div>

        <div class="input-wrapper">
          <textarea
            v-model="inputMessage"
            placeholder="메시지를 입력하세요..."
            rows="1"
            ref="textareaRef"
            @input="autoResize"
            @keydown="handleKeydown"
          ></textarea>
          <button
            class="send-button"
            :class="{ 'active': inputMessage.trim() }"
            :disabled="!inputMessage.trim()"
            @click="sendMessage"
          >
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 19V5M12 5L6 11M12 5L18 11" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>
        </div>
        <p class="input-hint">Enter로 전송, Shift+Enter로 줄바꿈</p>
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
  { text: '안녕하세요! 포트폴리오에 대해 궁금한 점이 있으시면 물어보세요.', isUser: false },
]);

const quickQuestions = [
  { id: 1, label: '개인정보', query: '개인정보에 대해 알려주세요' },
  { id: 2, label: 'PROMTREE', query: 'PROMTREE 프로젝트에 대해 알려주세요' },
  { id: 3, label: 'DailyPet', query: 'DailyPet 프로젝트에 대해 알려주세요' },
  { id: 4, label: 'CDD', query: 'CDD 프로젝트에 대해 알려주세요' },
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
      text: `${userText}에 대한 답변입니다.\n\n이 메시지는 데모용 응답입니다. 실제 서비스에서는 AI가 포트폴리오 관련 질문에 답변합니다.`,
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

<style scoped>
.chat-wrapper {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: #ffffff;
}

/* Messages Area */
.messages-area {
  flex: 1;
  overflow-y: auto;
  padding-bottom: 0.5rem;
}

.messages-container {
  max-width: 680px;
  margin: 0 auto;
  padding: 0.75rem;
}

/* Header */
.chat-header {
  padding: 1rem;
  border-bottom: 1px solid #e5e5e5;
  background-color: #ffffff;
  text-align: center;
}

.header-title {
  font-size: 1.1rem;
  font-weight: 600;
  color: #212121;
  margin: 0;
}

/* Message Row */
.message-row {
  padding: 0.75rem 0;
}

.message-row.user-row {
  display: flex;
  justify-content: flex-end;
}

.message-content {
  display: flex;
  align-items: flex-start;
  gap: 0.6rem;
  max-width: 85%;
}

.message-content.user-content {
  flex-direction: row;
}

/* Avatar */
.avatar-wrapper {
  flex-shrink: 0;
}

.avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1.5px solid;
}

.avatar svg {
  width: 18px;
  height: 18px;
}

.ai-avatar {
  border-color: #212121;
  color: #212121;
  background-color: #ffffff;
}

.user-avatar {
  border-color: #757575;
  color: #757575;
  background-color: #ffffff;
}

/* Message Body */
.message-body {
  flex: 1;
  min-width: 0;
}

.message-body.user-body {
  text-align: right;
}

.message-text {
  font-size: 0.9rem;
  line-height: 1.6;
  color: #212121;
  white-space: pre-wrap;
  word-break: break-word;
}

/* Typing Indicator */
.typing-indicator {
  display: flex;
  gap: 3px;
  padding: 4px 0;
}

.typing-indicator span {
  width: 6px;
  height: 6px;
  background-color: #9ca3af;
  border-radius: 50%;
  animation: typing 1.4s infinite ease-in-out;
}

.typing-indicator span:nth-child(1) { animation-delay: 0s; }
.typing-indicator span:nth-child(2) { animation-delay: 0.2s; }
.typing-indicator span:nth-child(3) { animation-delay: 0.4s; }

@keyframes typing {
  0%, 60%, 100% { transform: translateY(0); }
  30% { transform: translateY(-3px); }
}

/* Input Area */
.input-area {
  border-top: 1px solid #e5e5e5;
  background-color: #ffffff;
  padding: 0.75rem;
}

.input-container {
  max-width: 680px;
  margin: 0 auto;
}

/* Quick Questions */
.quick-questions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
  justify-content: center;
}

.quick-btn {
  padding: 0.4rem 0.9rem;
  font-size: 0.8rem;
  font-weight: 500;
  color: #424242;
  background-color: #ffffff;
  border: 1px solid #e0e0e0;
  border-radius: 1rem;
  cursor: pointer;
  transition: all 0.2s;
}

.quick-btn:hover {
  border-color: #212121;
  color: #212121;
  background-color: #f5f5f5;
}

.input-wrapper {
  display: flex;
  align-items: flex-end;
  gap: 0.5rem;
  padding: 0.5rem 0.75rem;
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  background-color: #ffffff;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.input-wrapper:focus-within {
  border-color: #212121;
}

.input-wrapper textarea {
  flex: 1;
  border: none;
  outline: none;
  resize: none;
  font-size: 0.9rem;
  line-height: 1.4;
  color: #212121;
  background: transparent;
  font-family: inherit;
  max-height: 150px;
}

.input-wrapper textarea::placeholder {
  color: #9ca3af;
}

.send-button {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: 1.5px solid #e0e0e0;
  background-color: #ffffff;
  color: #d0d0d0;
  cursor: not-allowed;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
  flex-shrink: 0;
}

.send-button svg {
  width: 16px;
  height: 16px;
}

.send-button.active {
  border-color: #212121;
  background-color: #212121;
  color: #ffffff;
  cursor: pointer;
}

.send-button.active:hover {
  background-color: #424242;
  border-color: #424242;
}

.input-hint {
  text-align: center;
  font-size: 0.7rem;
  color: #b0b0b0;
  margin-top: 0.4rem;
}

/* Scrollbar */
.messages-area::-webkit-scrollbar {
  width: 5px;
}

.messages-area::-webkit-scrollbar-track {
  background: transparent;
}

.messages-area::-webkit-scrollbar-thumb {
  background-color: #d1d5db;
  border-radius: 3px;
}

.messages-area::-webkit-scrollbar-thumb:hover {
  background-color: #9ca3af;
}

/* Responsive */
@media (max-width: 768px) {
  .messages-container,
  .input-container {
    padding-left: 0.75rem;
    padding-right: 0.75rem;
  }

  .welcome-title {
    font-size: 1.3rem;
  }
}
</style>
