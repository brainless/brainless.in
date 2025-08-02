const defaultTheme = require("tailwindcss/defaultTheme");

/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
	theme: {
		extend: {
			colors: {
				accent: "#2337ff",
				"accent-dark": "#000d8a",
				black: "rgb(15, 18, 25)",
				gray: "rgb(96, 115, 159)",
				"gray-light": "rgb(229, 233, 240)",
				"gray-dark": "rgb(34, 41, 57)",
			},
			fontFamily: {
				sans: ["Atkinson", ...defaultTheme.fontFamily.sans],
			},
			boxShadow: {
				DEFAULT:
					"0 2px 6px rgba(96, 115, 159, 25%), 0 8px 24px rgba(96, 115, 159, 33%), 0 16px 32px rgba(96, 115, 159, 33%)",
			},
		},
	},
	plugins: [],
};