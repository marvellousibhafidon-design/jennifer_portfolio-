import { getStore } from '@netlify/blobs';

export async function GET(request, { params }) {
  const { key } = params;
  const store = getStore('media');
  try {
    const blob = await store.get(key.join('/'));
    if (!blob) return new Response('Not found', { status: 404 });
    const ext = key.join('/').split('.').pop().toLowerCase();
    const contentTypeMap = { jpg: 'image/jpeg', jpeg: 'image/jpeg', png: 'image/png', webp: 'image/webp' };
    const contentType = contentTypeMap[ext] || 'application/octet-stream';
    return new Response(blob, { headers: { 'Content-Type': contentType, 'Cache-Control': 'public, max-age=31536000, immutable' } });
  } catch (error) {
    console.error('Image serve error:', error);
    return new Response('Internal server error', { status: 500 });
  }
}
