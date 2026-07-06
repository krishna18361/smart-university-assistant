/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        background: '#050816',
        surface: '#0B1120',
        surfaceLight: '#1E293B',
        primary: '#3B82F6',
        primaryLight: '#60A5FA',
        secondary: '#8B5CF6',
        accent: '#10B981',
        danger: '#EF4444',
        primaryText: '#F9FAFB',
        secondaryText: '#9CA3AF',
        borderColor: '#1E293B'
      },
      boxShadow: {
        'glow': '0 0 20px rgba(59, 130, 246, 0.3)',
        'card': '0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.2)'
      },
      animation: {
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'bounce-subtle': 'bounce 2s infinite'
      }
    },
  },
  plugins: [],
}
