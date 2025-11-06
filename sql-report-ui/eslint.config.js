import js from '@eslint/js'
import globals from 'globals'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'
import tseslint from 'typescript-eslint'
import path from 'path'
import { defineConfig, globalIgnores } from 'eslint/config'

export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    ignores: ['node_modules', 'dist'],
    extends: [
      js.configs.recommended,
      ...tseslint.configs.recommended,
      reactHooks.configs['recommended-latest'],
      reactRefresh.configs.vite,
    ],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
      parserOptions: {
        project: ['./tsconfig.app.json'], // 👈 conecta ESLint ao tsconfig
        tsconfigRootDir: path.resolve(),
      },
    },
    settings: {
      'import/resolver': {
        typescript: {
          project: ['./tsconfig.app.json'], // 👈 garante que o ESLint use o TS certo
        },
        alias: {
          map: [['@', './src']], // 👈 faz o ESLint entender o "@"
          extensions: ['.ts', '.tsx', '.js', '.jsx'],
        },
      },
    },
  },
])
