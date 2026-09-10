import { revalidatePath } from 'next/cache';

export async function POST(request) {
  const authHeader = request.headers.get('Authorization');
  const token = authHeader?.split('Bearer ')[1];
  if (token !== process.env.REVALIDATE_SECRET) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401, headers: { 'Content-Type': 'application/json' } });
  }
  try {
    const { path } = await request.json();
    if (!path) return new Response(JSON.stringify({ error: 'Missing path' }), { status: 400 });
    revalidatePath(path);
    return new Response(JSON.stringify({ success: true, revalidated: path }), { status: 200, headers: { 'Content-Type': 'application/json' } });
  } catch (error) {
    console.error('Revalidate error:', error);
    return new Response(JSON.stringify({ error: 'Revalidation failed' }), { status: 500, headers: { 'Content-Type': 'application/json' } });
  }
}
