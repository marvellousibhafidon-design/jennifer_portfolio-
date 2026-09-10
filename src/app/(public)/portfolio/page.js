import { db } from '@/lib/firebase/admin';
import Link from 'next/link';

export const revalidate = 3600;

async function getPortfolio() {
  const snapshot = await db.collection('portfolio')
    .where('isPublished', '==', true)
    .orderBy('order')
    .get();
  return snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
}

export default async function PortfolioPage() {
  const projects = await getPortfolio();

  const styles = {
    container: { maxWidth: '1200px', margin: '0 auto', padding: '40px 20px' },
    title: { fontSize: '2.5rem', color: '#C9A832', textAlign: 'center', marginBottom: '40px' },
    grid: { display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '24px' },
    card: { background: '#2D7D3A', borderRadius: '12px', overflow: 'hidden', border: '1px solid #3A8F48', transition: 'transform 0.2s', cursor: 'pointer', textDecoration: 'none', color: 'inherit' },
    cardImg: { width: '100%', height: '200px', objectFit: 'cover', borderBottom: '2px solid #C9A832' },
    cardContent: { padding: '20px' },
    cardTitle: { fontSize: '1.25rem', color: '#C9A832', marginBottom: '8px' },
    cardCat: { color: '#B8D9B8', margin: 0 },
    empty: { textAlign: 'center', padding: '60px 20px', color: '#B8D9B8' },
  };

  if (projects.length === 0) {
    return (
      <div style={styles.empty}>
        <h2 style={{ color: '#C9A832' }}>Portfolio</h2>
        <p>Projects coming soon.</p>
      </div>
    );
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Portfolio</h1>
      <div style={styles.grid}>
        {projects.map(p => (
          <Link href={`/portfolio/${p.slug}`} key={p.id} style={styles.card}>
            {p.coverImageUrl && <img src={p.coverImageUrl} alt={p.title} style={styles.cardImg} />}
            <div style={styles.cardContent}>
              <h3 style={styles.cardTitle}>{p.title}</h3>
              <p style={styles.cardCat}>{p.category}</p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
