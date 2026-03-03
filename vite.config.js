import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    outDir: 'static',
    assetsDir: '',
    rollupOptions: {
      input: {
        main: './src/sound_radar_classifier/core/client/main.ts',
        htmx: './src/sound_radar_classifier/core/client/htmx.ts',
        settings: './src/sound_radar_classifier/features/settings/client/settings.ts',
        radar: './src/sound_radar_classifier/features/radar/client/radar.ts',
      },
      output: {
        entryFileNames: '[name].js',
        chunkFileNames: '[name].js',
        assetFileNames: '[name].[ext]',
      },
    },
  },
})
