import { useState, useEffect, useRef } from 'react'
import axios from 'axios'

const API_BASE = 'http://localhost:5000/api'

function App() {
  const [chats, setChats] = useState([])
  const [currentChatId, setCurrentChatId] = useState(null)
  const [messages, setMessages] = useState([])
  const [inputText, setInputText] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [isAuthenticated, setIsAuthenticated] = useState(false)
  const [showAuth, setShowAuth] = useState('login') // 'login' or 'signup'
  const [authEmail, setAuthEmail] = useState('')
  const [authPassword, setAuthPassword] = useState('')
  const [authName, setAuthName] = useState('')
  const [selectedFile, setSelectedFile] = useState(null)
  const [showTools, setShowTools] = useState(false)
  const messagesEndRef = useRef(null)

  // Auto scroll to bottom of messages
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  // Load chats
  useEffect(() => {
    if (isAuthenticated) {
      fetchChats()
    }
  }, [isAuthenticated])

  // Load messages when current chat changes
  useEffect(() => {
    if (currentChatId && isAuthenticated) {
      fetchChatHistory(currentChatId)
    } else {
      setMessages([])
    }
  }, [currentChatId, isAuthenticated])

  const fetchChats = async () => {
    try {
      const response = await axios.get(`${API_BASE}/chats`)
      setChats(response.data)
    } catch (error) {
      console.error('Error fetching chats:', error)
    }
  }

  const fetchChatHistory = async (chatId) => {
    try {
      const response = await axios.get(`${API_BASE}/chats/${chatId}`)
      setMessages(response.data)
    } catch (error) {
      console.error('Error fetching chat history:', error)
    }
  }

  const createNewChat = async () => {
    try {
      const response = await axios.post(`${API_BASE}/chats`)
      setCurrentChatId(response.data.chat_id)
      fetchChats()
    } catch (error) {
      console.error('Error creating chat:', error)
    }
  }

  const deleteChat = async (chatId, e) => {
    e.stopPropagation()
    try {
      await axios.delete(`${API_BASE}/chats/${chatId}`)
      if (currentChatId === chatId) {
        setCurrentChatId(null)
      }
      fetchChats()
    } catch (error) {
      console.error('Error deleting chat:', error)
    }
  }

  const sendMessage = async (e) => {
    e.preventDefault()
    if (!inputText.trim() || !currentChatId) return

    const userMessage = inputText.trim()
    setInputText('')
    setIsLoading(true)

    try {
      const formData = new FormData()
      formData.append('question', userMessage)
      if (selectedFile) {
        formData.append('file', selectedFile)
        setSelectedFile(null)
      }

      const response = await axios.post(
        `${API_BASE}/chats/${currentChatId}/messages`,
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
      )
      fetchChatHistory(currentChatId)
      fetchChats()
    } catch (error) {
      console.error('Error sending message:', error)
    } finally {
      setIsLoading(false)
    }
  }

  const handleAuth = async (e) => {
    e.preventDefault()
    // For now, mock authentication
    setIsAuthenticated(true)
    setShowAuth(null)
  }

  const suggestedPrompts = [
    "Tell me about the attendance policy",
    "What scholarships are available?",
    "When are the exam schedules?",
    "How do I contact student support?"
  ]

  const universityTools = [
    { name: 'GPA Calculator', icon: '📊' },
    { name: 'Exam Countdown', icon: '⏰' },
    { name: 'Campus Map', icon: '🗺️' },
    { name: 'Academic Calendar', icon: '📅' },
    { name: 'Library Hours', icon: '📚' },
    { name: 'Course Catalog', icon: '📖' }
  ]

  const formatTime = (timestamp) => {
    if (!timestamp) return ''
    const date = new Date(timestamp)
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  }

  if (!isAuthenticated) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center p-4">
        <div className="w-full max-w-md">
          <div className="text-center mb-10">
            <div className="w-20 h-20 bg-gradient-to-br from-primary to-secondary rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-glow">
              <span className="text-4xl">🎓</span>
            </div>
            <h1 className="text-4xl font-bold text-primaryText mb-2">
              Smart University Assistant
            </h1>
            <p className="text-secondaryText">Your AI-powered academic companion</p>
          </div>

          <div className="bg-surface rounded-3xl p-8 shadow-card border border-borderColor">
            <div className="flex mb-8 bg-surfaceLight rounded-xl p-1">
              <button
                onClick={() => setShowAuth('login')}
                className={`flex-1 py-3 px-4 rounded-lg font-semibold transition-all ${
                  showAuth === 'login'
                    ? 'bg-primary text-white shadow-glow'
                    : 'text-secondaryText hover:text-primaryText'
                }`}
              >
                Login
              </button>
              <button
                onClick={() => setShowAuth('signup')}
                className={`flex-1 py-3 px-4 rounded-lg font-semibold transition-all ${
                  showAuth === 'signup'
                    ? 'bg-primary text-white shadow-glow'
                    : 'text-secondaryText hover:text-primaryText'
                }`}
              >
                Sign Up
              </button>
            </div>

            <form onSubmit={handleAuth} className="space-y-6">
              {showAuth === 'signup' && (
                <div>
                  <label className="block text-sm font-medium text-secondaryText mb-2">
                    Full Name
                  </label>
                  <input
                    type="text"
                    value={authName}
                    onChange={(e) => setAuthName(e.target.value)}
                    className="w-full bg-surfaceLight border border-borderColor rounded-xl px-4 py-3 text-primaryText placeholder-secondaryText focus:outline-none focus:border-primary focus:ring-2 focus:ring-primary/20 transition-all"
                    placeholder="Enter your full name"
                  />
                </div>
              )}

              <div>
                <label className="block text-sm font-medium text-secondaryText mb-2">
                  Email Address
                </label>
                <input
                  type="email"
                  value={authEmail}
                  onChange={(e) => setAuthEmail(e.target.value)}
                  className="w-full bg-surfaceLight border border-borderColor rounded-xl px-4 py-3 text-primaryText placeholder-secondaryText focus:outline-none focus:border-primary focus:ring-2 focus:ring-primary/20 transition-all"
                  placeholder="Enter your email"
                  required
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-secondaryText mb-2">
                  Password
                </label>
                <input
                  type="password"
                  value={authPassword}
                  onChange={(e) => setAuthPassword(e.target.value)}
                  className="w-full bg-surfaceLight border border-borderColor rounded-xl px-4 py-3 text-primaryText placeholder-secondaryText focus:outline-none focus:border-primary focus:ring-2 focus:ring-primary/20 transition-all"
                  placeholder="Enter your password"
                  required
                />
              </div>

              <button
                type="submit"
                className="w-full bg-gradient-to-r from-primary to-secondary text-white font-semibold py-4 rounded-xl hover:shadow-glow transition-all transform hover:scale-[1.02]"
              >
                {showAuth === 'login' ? 'Login' : 'Create Account'}
              </button>
            </form>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="flex h-screen bg-background">
      {/* Sidebar */}
      <div className={`${showTools ? 'w-80' : 'w-64'} bg-surface border-r border-borderColor flex flex-col transition-all duration-300`}>
        {/* Header */}
        <div className="p-6 border-b border-borderColor">
          <div className="flex items-center justify-between mb-6">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-gradient-to-br from-primary to-secondary rounded-xl flex items-center justify-center shadow-glow">
                <span className="text-xl">🎓</span>
              </div>
              <h1 className="text-xl font-bold text-primaryText">Smart Assistant</h1>
            </div>
            <button
              onClick={() => setShowTools(!showTools)}
              className="p-2 rounded-lg hover:bg-surfaceLight text-secondaryText hover:text-primaryText transition-all"
            >
              {showTools ? '✕' : '⚙️'}
            </button>
          </div>

          <button
            onClick={createNewChat}
            className="w-full bg-gradient-to-r from-primary to-secondary text-white font-semibold py-3 px-4 rounded-xl hover:shadow-glow transition-all transform hover:scale-[1.02] flex items-center justify-center gap-2"
          >
            <span className="text-lg">+</span>
            New Chat
          </button>
        </div>

        {/* Chats List */}
        <div className="flex-1 overflow-y-auto px-4 py-4">
          <h2 className="text-xs font-semibold text-secondaryText uppercase tracking-wider mb-3 px-2">
            Recent Chats
          </h2>
          {chats.map((chat) => (
            <div
              key={chat.chat_id}
              onClick={() => setCurrentChatId(chat.chat_id)}
              className={`p-4 rounded-xl mb-2 cursor-pointer transition-all group ${
                currentChatId === chat.chat_id
                  ? 'bg-gradient-to-r from-primary/20 to-secondary/20 border border-primary/30'
                  : 'hover:bg-surfaceLight border border-transparent hover:border-borderColor'
              }`}
            >
              <div className="flex justify-between items-start">
                <div className="flex-1 min-w-0">
                  <p className="text-sm font-medium text-primaryText truncate">
                    {chat.title}
                  </p>
                  <p className="text-xs text-secondaryText mt-1">
                    {chat.last_updated ? new Date(chat.last_updated).toLocaleDateString() : ''}
                  </p>
                </div>
                <button
                  onClick={(e) => deleteChat(chat.chat_id, e)}
                  className="opacity-0 group-hover:opacity-100 text-secondaryText hover:text-danger transition-all ml-2 p-1 rounded"
                >
                  🗑️
                </button>
              </div>
            </div>
          ))}
        </div>

        {/* University Tools (conditionally shown) */}
        {showTools && (
          <div className="border-t border-borderColor p-4">
            <h2 className="text-xs font-semibold text-secondaryText uppercase tracking-wider mb-3 px-2">
              University Tools
            </h2>
            <div className="space-y-2">
              {universityTools.map((tool, index) => (
                <button
                  key={index}
                  className="w-full p-3 rounded-xl hover:bg-surfaceLight text-left transition-all flex items-center gap-3 border border-transparent hover:border-borderColor"
                >
                  <span className="text-xl">{tool.icon}</span>
                  <span className="text-sm font-medium text-primaryText">{tool.name}</span>
                </button>
              ))}
            </div>
          </div>
        )}

        {/* User Profile */}
        <div className="p-4 border-t border-borderColor">
          <div className="flex items-center gap-3 p-3 rounded-xl hover:bg-surfaceLight cursor-pointer transition-all">
            <div className="w-10 h-10 bg-gradient-to-br from-accent to-primary rounded-full flex items-center justify-center">
              <span className="font-bold text-white">U</span>
            </div>
            <div className="flex-1">
              <p className="text-sm font-medium text-primaryText">Student User</p>
              <p className="text-xs text-secondaryText">student@university.edu</p>
            </div>
            <button
              onClick={() => setIsAuthenticated(false)}
              className="text-secondaryText hover:text-danger transition-all"
            >
              🚪
            </button>
          </div>
        </div>
      </div>

      {/* Main Chat Area */}
      <div className="flex-1 flex flex-col">
        {/* Chat Messages */}
        <div className="flex-1 overflow-y-auto p-6">
          {!currentChatId ? (
            <div className="max-w-4xl mx-auto text-center mt-10">
              <div className="w-32 h-32 bg-gradient-to-br from-primary to-secondary rounded-3xl flex items-center justify-center mx-auto mb-10 shadow-glow animate-pulse-slow">
                <span className="text-6xl">🎓</span>
              </div>
              <h2 className="text-4xl font-bold text-primaryText mb-4">
                Welcome to Smart University Assistant!
              </h2>
              <p className="text-xl text-secondaryText mb-12">
                Your AI-powered companion for all academic needs
              </p>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 max-w-2xl mx-auto">
                {suggestedPrompts.map((prompt, index) => (
                  <button
                    key={index}
                    onClick={() => {
                      createNewChat().then(() => {
                        setTimeout(() => {
                          setInputText(prompt)
                        }, 100)
                      })
                    }
                    }
                    className="p-6 bg-surface border border-borderColor rounded-2xl hover:border-primary hover:shadow-glow transition-all text-left group"
                  >
                    <p className="text-primaryText font-medium group-hover:text-primary transition-colors">
                      {prompt}
                    </p>
                  </button>
                ))}
              </div>
            </div>
          ) : (
            <div className="max-w-4xl mx-auto">
              {messages.length === 0 ? (
                <div className="text-center mt-20">
                  <div className="w-24 h-24 bg-gradient-to-br from-primary/20 to-secondary/20 rounded-2xl flex items-center justify-center mx-auto mb-6">
                    <span className="text-4xl">💬</span>
                  </div>
                  <h3 className="text-2xl font-semibold text-primaryText mb-2">
                    Start a conversation
                  </h3>
                  <p className="text-secondaryText">
                    Ask me anything about university life!
                  </p>
                </div>
              ) : (
                <div className="space-y-8">
                  {messages.map((msg, index) => (
                    <div
                      key={index}
                      className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
                    >
                      <div className={`max-w-[80%] ${msg.role === 'user' ? 'items-end' : 'items-start'} flex gap-4`}>
                        {msg.role === 'assistant' && (
                          <div className="w-10 h-10 bg-gradient-to-br from-primary to-secondary rounded-xl flex items-center justify-center flex-shrink-0 shadow-glow">
                            <span className="text-lg">🤖</span>
                          </div>
                        )}
                        <div className={`${msg.role === 'user' ? 'order-2' : ''}`}>
                          <div
                            className={`p-5 rounded-2xl shadow-card ${
                              msg.role === 'user'
                                ? 'bg-gradient-to-r from-primary to-secondary text-white'
                                : 'bg-surface border border-borderColor text-primaryText'
                            }`}
                          >
                            <p className="whitespace-pre-wrap leading-relaxed">
                              {msg.role === 'user' ? msg.question : msg.answer}
                            </p>
                          </div>
                          <p className="text-xs text-secondaryText mt-2 px-1">
                            {formatTime(msg.timestamp)}
                          </p>
                        </div>
                        {msg.role === 'user' && (
                          <div className="w-10 h-10 bg-gradient-to-br from-accent to-primary rounded-xl flex items-center justify-center flex-shrink-0 shadow-glow order-1">
                            <span className="text-lg font-bold text-white">U</span>
                          </div>
                        )}
                      </div>
                    </div>
                  ))}

                  {isLoading && (
                    <div className="flex justify-start">
                      <div className="flex gap-4">
                        <div className="w-10 h-10 bg-gradient-to-br from-primary to-secondary rounded-xl flex items-center justify-center shadow-glow animate-pulse-slow">
                          <span className="text-lg">🤖</span>
                        </div>
                        <div className="bg-surface border border-borderColor p-5 rounded-2xl shadow-card">
                          <div className="flex gap-2">
                            <div className="w-2 h-2 bg-primary rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
                            <div className="w-2 h-2 bg-primary rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
                            <div className="w-2 h-2 bg-primary rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
                          </div>
                        </div>
                      </div>
                    </div>
                  )}
                  <div ref={messagesEndRef} />
                </div>
              )}
            </div>
          )}
        </div>

        {/* Input Area */}
        {currentChatId && (
          <div className="p-6 border-t border-borderColor">
            <div className="max-w-4xl mx-auto">
              {selectedFile && (
                <div className="mb-4 p-4 bg-surface border border-borderColor rounded-xl flex items-center justify-between">
                  <div className="flex items-center gap-3">
                    <span className="text-2xl">📄</span>
                    <span className="text-primaryText text-sm">{selectedFile.name}</span>
                  </div>
                  <button
                    onClick={() => setSelectedFile(null)}
                    className="text-secondaryText hover:text-danger transition-all"
                  >
                    ✕
                  </button>
                </div>
              )}
              <form onSubmit={sendMessage} className="relative">
                <div className="bg-surface border border-borderColor rounded-2xl p-2 flex items-end gap-2 focus-within:border-primary focus-within:ring-2 focus-within:ring-primary/20 transition-all shadow-card">
                  <input
                    type="file"
                    id="file-upload"
                    className="hidden"
                    onChange={(e) => setSelectedFile(e.target.files[0])}
                  />
                  <label
                    htmlFor="file-upload"
                    className="p-3 rounded-xl hover:bg-surfaceLight text-secondaryText hover:text-primary cursor-pointer transition-all"
                  >
                    📎
                  </label>
                  <input
                    type="text"
                    value={inputText}
                    onChange={(e) => setInputText(e.target.value)}
                    disabled={isLoading}
                    placeholder="Type your message..."
                    className="flex-1 bg-transparent border-none text-primaryText placeholder-secondaryText focus:outline-none py-3 px-2 resize-none"
                  />
                  <button
                    type="submit"
                    disabled={!inputText.trim() || isLoading}
                    className="p-3 bg-gradient-to-r from-primary to-secondary text-white rounded-xl hover:shadow-glow transition-all disabled:opacity-50 disabled:cursor-not-allowed transform hover:scale-105"
                  >
                    {isLoading ? '⏳' : '➤'}
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default App
