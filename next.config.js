/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    serverActions: {
      allowedOrigins: ['localhost:3000'],
    },
  },
  serverExternalPackages: ['jsdom', 'dompurify'], // Prevent bundling on client
  images: {
    remotePatterns: [],
  },
};
module.exports = nextConfig;