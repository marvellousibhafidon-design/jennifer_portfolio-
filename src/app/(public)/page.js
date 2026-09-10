import { db } from '@/lib/firebase/admin';

export const revalidate = 3600;

async function getHomepageData() {
  const homepageDoc = await db.collection('homepage').doc('singleton').get();
  const featuredProjects = await db.collection('portfolio')
    .where('isPublished', '==', true)
    .where('isFeatured', '==', true)
    .get();
  return {
    homepage: homepageDoc.exists ? homepageDoc.data() : null,
    featuredProjects: featuredProjects.docs.map(doc => ({ id: doc.id, ...doc.data() })),
  };
}

export default async function HomePage() {
  const { homepage, featuredProjects } = await getHomepageData();

  const styles = {
    hero: { background: 'linear-gradient(135deg, #0D2E17, #1A4D24, #2D7D3A)', padding: '80px 20px', textAlign: 'center', borderBottom: '3px solid #C9A832' },
    heroTitle: { fontSize: '3rem', fontWeight: 'bold', marginBottom: '1rem', color: '#C9A832', textShadow: '0 2px 4px rgba(0,0,0,0.3)' },
    heroSub: { fontSize: '1.25rem', marginBottom: '2rem', color: '#E8E8E8', opacity: 0.95 },
    goldBtn: { display: 'inline-block', padding: '14px 40px', background: '#C9A832', color: '#0D2E17', borderRadius: '50px', fontWeight: 'bold', textDecoration: 'none', fontSize: '1rem' },
    section: { padding: '60px 20px', maxWidth: '1200px', margin: '0 auto' },
    sectionTitle: { fontSize: '2rem', textAlign: 'center', color: '#C9A832', marginBottom: '40px' },
    grid: { display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '24px' },
    card: { background: '#2D7D3A', borderRadius: '12px', overflow: 'hidden', boxShadow: '0 4px 20px rgba(0,0,0,0.3)', border: '1px solid #3A8F48' },
    cardImg: { width: '100%', height: '200px', objectFit: 'cover', borderBottom: '2px solid #C9A832' },
    cardContent: { padding: '20px' },
    cardTitle: { fontSize: '1.25rem', color: '#C9A832', marginBottom: '8px' },
    cardCat: { color: '#B8D9B8', margin: 0 },
    ctaSection: { padding: '60px 20px', background: '#1A4D24', textAlign: 'center', borderTop: '3px solid #C9A832', borderBottom: '3px solid #C9A832' },
    ctaTitle: { fontSize: '2rem', color: '#C9A832', marginBottom: '16px' },
    ctaBtn: { display: 'inline-block', padding: '14px 40px', background: '#C9A832', color: '#0D2E17', borderRadius: '50px', fontWeight: 'bold', textDecoration: 'none', fontSize: '1rem' },
    empty: { textAlign: 'center', color: '#B8D9B8', fontSize: '1.1rem', padding: '20px' },
  };

  return (
    <>
      <section style={styles.hero}>
        <div style={{ maxWidth: '800px', margin: '0 auto' }}>
          <h1 style={styles.heroTitle}>{homepage?.heroTitle || 'Your Ideas, Crafted into Writing'}</h1>
          <p style={styles.heroSub}>{homepage?.heroSubtext || 'Partner with me to bring your story to life.'}</p>
          <a href="/contact" style={styles.goldBtn}>{homepage?.heroCtaText || 'Work With Me'}</a>
        </div>
      </section>

      <section style={styles.section}>
        <h2 style={styles.sectionTitle}>Featured Work</h2>
        {featuredProjects.length > 0 ? (
          <div style={styles.grid}>
            {featuredProjects.map(p => (
              <div key={p.id} style={styles.card}>
                {p.coverImageUrl && <img src={p.coverImageUrl} alt={p.title} style={styles.cardImg} />}
                <div style={styles.cardContent}>
                  <h3 style={styles.cardTitle}>{p.title}</h3>
                  <p style={styles.cardCat}>{p.category}</p>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <p style={styles.empty}>✨ Portfolio projects will appear here once Jennifer adds them from the admin panel.</p>
        )}
      </section>

      <section style={styles.ctaSection}>
        <div style={{ maxWidth: '600px', margin: '0 auto' }}>
          <h2 style={styles.ctaTitle}>Ready to work together?</h2>
          <a href="/contact" style={styles.ctaBtn}>Let's Talk</a>
        </div>
      </section>
    </>
  );
}
