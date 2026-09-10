import { db } from '@/lib/firebase/admin';

export const revalidate = 3600;

async function getAboutData() {
  const doc = await db.collection('about').doc('singleton').get();
  return doc.exists ? doc.data() : null;
}

export default async function AboutPage() {
  const about = await getAboutData();

  const styles = {
    container: { maxWidth: '900px', margin: '0 auto', padding: '40px 20px' },
    title: { fontSize: '2.5rem', color: '#C9A832', marginBottom: '20px' },
    image: { width: '100%', maxWidth: '300px', borderRadius: '12px', marginBottom: '30px', border: '3px solid #C9A832' },
    bio: { fontSize: '1.1rem', lineHeight: '1.8', marginBottom: '30px', color: '#E8E8E8' },
    philosophy: { fontSize: '1.1rem', lineHeight: '1.8', marginBottom: '30px', background: '#2D7D3A', padding: '30px', borderRadius: '12px', border: '1px solid #3A8F48', color: '#E8E8E8' },
    philosophyTitle: { color: '#C9A832', marginBottom: '10px' },
    specialties: { background: '#0D2E17', padding: '20px 30px', borderRadius: '12px', border: '1px solid #C9A832' },
    specialtiesTitle: { fontSize: '1.2rem', fontWeight: 'bold', color: '#C9A832', marginBottom: '10px' },
    tag: { display: 'inline-block', background: '#2D7D3A', color: '#C9A832', padding: '6px 16px', borderRadius: '20px', margin: '4px 6px 4px 0', fontSize: '0.9rem', border: '1px solid #C9A832' },
    empty: { textAlign: 'center', padding: '60px 20px', color: '#B8D9B8' },
  };

  if (!about) {
    return (
      <div style={styles.empty}>
        <h2 style={{ color: '#C9A832' }}>About Jennifer</h2>
        <p>Professional biography coming soon.</p>
      </div>
    );
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>About Jennifer</h1>
      {about.profileImageUrl && <img src={about.profileImageUrl} alt="Jennifer Ibhafidon" style={styles.image} />}
      {about.biography && <div style={styles.bio} dangerouslySetInnerHTML={{ __html: about.biography }} />}
      {about.philosophy && (
        <div style={styles.philosophy}>
          <h3 style={styles.philosophyTitle}>Writing Philosophy</h3>
          <div dangerouslySetInnerHTML={{ __html: about.philosophy }} />
        </div>
      )}
      {about.specialties && about.specialties.length > 0 && (
        <div style={styles.specialties}>
          <h3 style={styles.specialtiesTitle}>Specialties</h3>
          {about.specialties.map((s, i) => <span key={i} style={styles.tag}>{s}</span>)}
        </div>
      )}
    </div>
  );
}
