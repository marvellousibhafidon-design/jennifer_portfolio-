import { db } from '@/lib/firebase/admin';

export const revalidate = 3600;

async function getServices() {
  const snapshot = await db.collection('services')
    .where('isPublished', '==', true)
    .orderBy('order')
    .get();
  return snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
}

export default async function ServicesPage() {
  const services = await getServices();

  const styles = {
    container: { maxWidth: '1000px', margin: '0 auto', padding: '40px 20px' },
    title: { fontSize: '2.5rem', color: '#C9A832', textAlign: 'center', marginBottom: '40px' },
    grid: { display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '24px' },
    card: { background: '#2D7D3A', padding: '30px', borderRadius: '12px', boxShadow: '0 4px 20px rgba(0,0,0,0.3)', border: '1px solid #3A8F48' },
    cardTitle: { fontSize: '1.3rem', color: '#C9A832', marginBottom: '10px' },
    cardDesc: { fontSize: '1rem', lineHeight: '1.6', color: '#B8D9B8' },
    cardCta: { display: 'inline-block', marginTop: '16px', color: '#C9A832', fontWeight: 'bold', textDecoration: 'none' },
    empty: { textAlign: 'center', padding: '60px 20px', color: '#B8D9B8' },
  };

  if (services.length === 0) {
    return (
      <div style={styles.empty}>
        <h2 style={{ color: '#C9A832' }}>Services</h2>
        <p>Service details coming soon.</p>
      </div>
    );
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Services</h1>
      <div style={styles.grid}>
        {services.map(service => (
          <div key={service.id} style={styles.card}>
            <h3 style={styles.cardTitle}>{service.title}</h3>
            <div style={styles.cardDesc} dangerouslySetInnerHTML={{ __html: service.description }} />
            <a href={service.ctaLink || '/contact'} style={styles.cardCta}>{service.ctaText || 'Learn More'} →</a>
          </div>
        ))}
      </div>
    </div>
  );
}
