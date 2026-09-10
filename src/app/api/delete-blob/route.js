import { auth } from '@/lib/firebase/admin';
import { getStore } from '@netlify/blobs';

export async function POST(request) {
  const authHeader = request.headers.get('Authorization');
  const token = authHeader?.split('Bearer ')[1];
  if (!token) return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  let decodedToken;
  try { decodedToken = await auth.verifyIdToken(token); if (!decodedToken.admin) return new Response(JSON.stringify({ error: 'Forbidden' }), { status: 403 }); } catch { return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 }); }
  const { key } = await request.json();
  if (!key) return new Response(JSON.stringify({ error: 'Missing key' }), { status: 400 });
  try {
    const store = getStore('media');
    await store.delete(key);
    return new Response(JSON.stringify({ success: true }), { status: 200, headers: { 'Content-Type': 'application/json' } });
  } catch (error) {
    console.error('Delete error:', error);
    return new Response(JSON.stringify({ error: 'Delete failed' }), { status: 500 });
  }
}
