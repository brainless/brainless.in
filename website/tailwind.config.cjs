const defaultTheme = require("tailwindcss/defaultTheme");

/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
	theme: {
		extend: {
			colors: {
				accent: "#2337ff",
				"accent-dark": "#000d8a",
				gray: "rgb(96, 115, 159)",
			},
			fontFamily: {
				sans: ["Funnel Sans", ...defaultTheme.fontFamily.sans],
				serif: ["Barriecito", ...defaultTheme.fontFamily.serif],
			},
			boxShadow: {
				DEFAULT:
					"0 2px 6px rgba(96, 115, 159, 25%), 0 8px 24px rgba(96, 115, 159, 33%), 0 16px 32px rgba(96, 115, 159, 33%)",
			},
		},
	},
	plugins: [require("@tailwindcss/typography")],
};