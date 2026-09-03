/// <reference types="vite/client" />
interface ImportMetaEnv { readonly VITE_API_URL?: string; readonly VITE_VOO_REFRESH_INTERVAL?: string; readonly VITE_MAX_GLOBE_AIRCRAFT?: string; readonly VITE_MAX_GLOBE_ROUTES?: string }
interface ImportMeta { readonly env: ImportMetaEnv }
