import { auth, db } from '@/lib/firebase/admin';
import { getStore } from '@netlify/blobs';

export async function DELETE(request, { params }) {
  const { id } = params;
  const authHeader = request.headers.get('Authorization');
  const token = authHeader?.split('Bearer ')[1];
  if (!token) return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  let decodedToken;
  try { decodedToken = await auth.verifyIdToken(token); if (!decodedToken.admin) return new Response(JSON.stringify({ error: 'Forbidden' }), { status: 403 }); } catch { return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 }); }
  const doc = await db.collection('portfolio').doc(id).get();
  if (!doc.exists) return new Response(JSON.stringify({ error: 'Not found' }), { status: 404 });
  const data = doc.data();
  const blobKeys = [];
  if (data.coverImageUrl) { const match = data.coverImageUrl.match(/\/api\/image\/(.+)/); if (match) blobKeys.push(match[1]); }
  if (data.galleryImages) {
    for (const url of data.galleryImages) { const match = url.match(/\/api\/image\/(.+)/); if (match) blobKeys.push(match[1]); }
  }
  await db.collection('portfolio').doc(id).delete();
  const store = getStore('media');
  const deleteErrors = [];
  for (const key of blobKeys) {
    try { await store.delete(key); } catch (err) { console.error(`Failed to delete ${key}:`, err); deleteErrors.push(key); }
  }
  return new Response(JSON.stringify({ success: true, deletedBlobs: blobKeys.length - deleteErrors.length, errors: deleteErrors.length > 0 ? deleteErrors : undefined }), { status: 200, headers: { 'Content-Type': 'application/json' } });
}
