/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html'
  ],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['IBM Plex Sans', 'sans-serif'], // Ini buat IBM Plex Sans
        'fifa': ['fifa-26', 'sans-serif'],     // Ini buat FIFA26
      },
    },
  },
  plugins: [],
}