/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './apps/accounts/templates/**/*.html',
    './apps/okr_space/templates/**/*.html',
    './node_modules/flowbite/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin'),
  ],
}

