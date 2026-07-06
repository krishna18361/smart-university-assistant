/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        background: '#0B1120',
        surface: '#1F2937',
        primaryText: '#E5E7EB',
        borderColor: '#374151'
      }
    },
  },
  plugins: [],
}
