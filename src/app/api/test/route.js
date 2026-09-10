import { db } from '@/lib/firebase/admin';

export async function GET() {
  try {
    const doc = await db.collection('siteSettings').doc('singleton').get();
    const data = doc.exists ? doc.data() : null;
    return new Response(JSON.stringify({ success: true, data }), { status: 200, headers: { 'Content-Type': 'application/json' } });
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), { status: 500, headers: { 'Content-Type': 'application/json' } });
  }
}
