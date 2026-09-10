import { auth } from '@/lib/firebase/admin';
import { getStore } from '@netlify/blobs';
import { randomUUID } from 'crypto';

const ALLOWED_TYPES = ['image/jpeg', 'image/png', 'image/webp'];
const MAX_SIZE = 5 * 1024 * 1024;

export async function POST(request) {
  const authHeader = request.headers.get('Authorization');
  const token = authHeader?.split('Bearer ')[1];
  if (!token) return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  let decodedToken;
  try { decodedToken = await auth.verifyIdToken(token); if (!decodedToken.admin) return new Response(JSON.stringify({ error: 'Forbidden' }), { status: 403 }); } catch { return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 }); }
  const formData = await request.formData();
  const file = formData.get('file');
  const path = formData.get('path');
  if (!file || !path) return new Response(JSON.stringify({ error: 'Missing file or path' }), { status: 400 });
  if (!ALLOWED_TYPES.includes(file.type)) return new Response(JSON.stringify({ error: 'Invalid file type. Allowed: JPEG, PNG, WebP' }), { status: 400 });
  if (file.size > MAX_SIZE) return new Response(JSON.stringify({ error: 'File too large. Max: 5MB' }), { status: 400 });
  const store = getStore('media');
  const key = `${path}/${randomUUID()}.${file.name.split('.').pop()}`;
  try {
    await store.set(key, Buffer.from(await file.arrayBuffer()));
    return new Response(JSON.stringify({ success: true, key }), { status: 200, headers: { 'Content-Type': 'application/json' } });
  } catch (error) {
    console.error('Upload error:', error);
    return new Response(JSON.stringify({ error: 'Upload failed' }), { status: 500 });
  }
}
