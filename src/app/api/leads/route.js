import { db } from '@/lib/firebase/admin';

const rateLimit = new Map();

function getClientIP(request) {
  const forwarded = request.headers.get('x-forwarded-for');
  return forwarded ? forwarded.split(',')[0] : 'unknown';
}

function isRateLimited(ip) {
  const now = Date.now();
  const window = 3600000;
  const maxRequests = 5;
  if (!rateLimit.has(ip)) rateLimit.set(ip, []);
  const timestamps = rateLimit.get(ip).filter(t => now - t < window);
  timestamps.push(now);
  rateLimit.set(ip, timestamps);
  return timestamps.length > maxRequests;
}

export async function POST(request) {
  const ip = getClientIP(request);
  if (isRateLimited(ip)) {
    return new Response(JSON.stringify({ error: 'Too many requests' }), { status: 429, headers: { 'Content-Type': 'application/json' } });
  }
  let body;
  try { body = await request.json(); } catch { return new Response(JSON.stringify({ error: 'Invalid JSON' }), { status: 400, headers: { 'Content-Type': 'application/json' } }); }
  const { name, email, projectType, description, timeline } = body;
  if (!name || name.length > 100) return new Response(JSON.stringify({ error: 'Name required (max 100 chars)' }), { status: 400, headers: { 'Content-Type': 'application/json' } });
  if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return new Response(JSON.stringify({ error: 'Valid email required' }), { status: 400, headers: { 'Content-Type': 'application/json' } });
  if (!description || description.length > 5000) return new Response(JSON.stringify({ error: 'Description required (max 5000 chars)' }), { status: 400, headers: { 'Content-Type': 'application/json' } });
  try {
    await db.collection('leads').add({ name: name.trim(), email: email.trim(), projectType: projectType || null, description: description.trim(), timeline: timeline || null, status: 'new', createdAt: new Date().toISOString() });
    return new Response(JSON.stringify({ success: true }), { status: 200, headers: { 'Content-Type': 'application/json' } });
  } catch (err) {
    console.error('Lead error:', err);
    return new Response(JSON.stringify({ error: 'Internal server error' }), { status: 500, headers: { 'Content-Type': 'application/json' } });
  }
}
