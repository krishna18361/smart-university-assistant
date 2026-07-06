import { useState, useEffect, useRef } from 'react'
import axios from 'axios'

const API_BASE = 'http://localhost:5000/api'

function App() {
  const [chats, setChats] = useState([])
  const [currentChatId, setCurrentChatId] = useState(null)
  const [messages, setMessages] = useState([])
  const [inputText, setInputText] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const messagesEndRef = useRef(null)

  // Auto scroll to bottom of messages
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  // Load all chats on initial render
  useEffect(() => {
    fetchChats()
  }, [])

  // Load messages when current chat changes
  useEffect(() => {
    if (currentChatId) {
      fetchChatHistory(currentChatId)
    } else {
      setMessages([])
    }
  }, [currentChatId])

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
      const response = await axios.post(
        `${API_BASE}/chats/${currentChatId}/messages`,
        { question: userMessage }
      )
      fetchChatHistory(currentChatId)
      fetchChats()
    } catch (error) {
      console.error('Error sending message:', error)
    } finally {
      setIsLoading(false)
    }
  }

  const suggestedPrompts = [
    "Tell me about the attendance policy",
    "What scholarships are available?",
    "When are the exam schedules?",
    "How do I contact student support?"
  ]

  return (
    <div className="flex h-screen bg-background">
      {/* Sidebar */}
      <div className="w-64 bg-surface border-r border-borderColor flex flex-col">
        <div className="p-4">
          <h1 className="text-xl font-bold text-primaryText mb-4">Smart Assistant</h1>
          <button
            onClick={createNewChat}
            className="w-full bg-blue-600 hover:bg-blue-700 text-white py-2 px-4 rounded-lg transition-colors mb-4"
          >
            + New Chat
          </button>
        </div>

        <div className="flex-1 overflow-y-auto px-4">
          <h2 className="text-sm font-semibold text-gray-400 mb-2">Recent Chats</h2>
          {chats.map((chat) => (
            <div
              key={chat.chat_id}
              onClick={() => setCurrentChatId(chat.chat_id)}
              className={`p-3 rounded-lg mb-2 cursor-pointer transition-colors ${
                currentChatId === chat.chat_id 
                  ? 'bg-blue-600/20 border border-blue-600' 
                  : 'hover:bg-borderColor'
              }`}
            >
              <div className="flex justify-between items-start">
                <div className="flex-1">
                  <p className="text-sm text-primaryText truncate">{chat.title}</p>
                  <p className="text-xs text-gray-500 mt-1">{chat.last_updated.slice(0, 10)}</p>
                </div>
                <button
                  onClick={(e) => deleteChat(chat.chat_id, e)}
                  className="text-gray-400 hover:text-red-500 ml-2"
                >
                  ×
                </button>
              </div>
            </div>
          ))}
        </div>

        <div className="p-4 border-t border-borderColor">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-blue-600 rounded-full flex items-center justify-center">
              <span className="font-bold">U</span>
            </div>
            <div>
              <p className="text-sm text-primaryText">Student User</p>
              <p className="text-xs text-gray-400">student@university.edu</p>
            </div>
          </div>
        </div>
      </div>

      {/* Main Chat Area */}
      <div className="flex-1 flex flex-col">
        {/* Chat Messages */}
        <div className="flex-1 overflow-y-auto p-6">
          {!currentChatId ? (
            <div className="max-w-3xl mx-auto text-center mt-20">
              <h2 className="text-3xl font-bold text-primaryText mb-2">Welcome!</h2>
              <p className="text-gray-400 mb-8">How can I help you today?</p>
              
              <div className="grid grid-cols-2 gap-4">
                {suggestedPrompts.map((prompt, index) => (
                  <button
                    key={index}
                    onClick={() => {
                      createNewChat().then(() => {
                        setTimeout(() => {
                          setInputText(prompt)
                        }, 100)
                      })
                    }}
                    className="p-4 bg-surface border border-borderColor rounded-lg hover:border-blue-600 transition-colors text-left"
                  >
                    <p className="text-primaryText text-sm">{prompt}</p>
                  </button>
                ))}
              </div>
            </div>
          ) : (
            <div className="max-w-3xl mx-auto">
              {messages.length === 0 ? (
                <div className="text-center mt-20">
                  <h3 className="text-xl font-semibold text-primaryText mb-2">Start a conversation</h3>
                  <p className="text-gray-400">Ask me anything about university life!</p>
                </div>
              ) : (
                messages.map((msg, index) => (
                  <div key={index} className={`mb-6 ${msg.role === 'user' ? 'text-right' : ''}`}>
                    <div
                      className={`inline-block max-w-[80%] p-4 rounded-lg ${
                        msg.role === 'user'
                          ? 'bg-blue-600 text-white'
                          : 'bg-surface border border-borderColor text-primaryText'
                      }`}
                    >
                      <p className="whitespace-pre-wrap">{msg.role === 'user' ? msg.question : msg.answer}</p>
                    </div>
                  </div>
                ))
              )}
              
              {isLoading && (
                <div className="mb-6">
                  <div className="inline-block bg-surface border border-borderColor rounded-lg p-4">
                    <div className="flex gap-2">
                      <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></div>
                      <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></div>
                      <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></div>
                    </div>
                  </div>
                </div>
              )}
              <div ref={messagesEndRef} />
            </div>
          )}
        </div>

        {/* Input Area */}
        <div className="p-6 border-t border-borderColor">
          <form onSubmit={sendMessage} className="max-w-3xl mx-auto">
            <div className="relative">
              <input
                type="text"
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
                disabled={!currentChatId || isLoading}
                placeholder={currentChatId ? "Type your message..." : "Start a new chat first"}
                className="w-full bg-surface border border-borderColor rounded-full py-3 px-5 pr-14 text-primaryText placeholder-gray-500 focus:outline-none focus:border-blue-600 disabled:opacity-50"
              />
              <button
                type="submit"
                disabled={!inputText.trim() || !currentChatId || isLoading}
                className="absolute right-2 top-1/2 -translate-y-1/2 bg-blue-600 hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed text-white w-10 h-10 rounded-full flex items-center justify-center"
              >
                →
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  )
}

export default App
