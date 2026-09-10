import { db } from '@/lib/firebase/admin';

export const revalidate = 3600;

async function getProcessStages() {
  const snapshot = await db.collection('processStages')
    .where('isPublished', '==', true)
    .orderBy('order')
    .get();
  return snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
}

export default async function ProcessPage() {
  const stages = await getProcessStages();

  const styles = {
    container: { maxWidth: '800px', margin: '0 auto', padding: '40px 20px' },
    title: { fontSize: '2.5rem', color: '#C9A832', textAlign: 'center', marginBottom: '40px' },
    step: { display: 'flex', alignItems: 'flex-start', gap: '20px', marginBottom: '30px', background: '#2D7D3A', padding: '20px', borderRadius: '12px', border: '1px solid #3A8F48' },
    number: { fontSize: '2rem', fontWeight: 'bold', color: '#C9A832', minWidth: '50px' },
    content: { flex: 1 },
    stepTitle: { fontSize: '1.3rem', color: '#C9A832', marginBottom: '6px' },
    stepDesc: { color: '#E8E8E8', lineHeight: '1.6' },
    empty: { textAlign: 'center', padding: '60px 20px', color: '#B8D9B8' },
  };

  if (stages.length === 0) {
    return (
      <div style={styles.empty}>
        <h2 style={{ color: '#C9A832' }}>My Writing Process</h2>
        <p>Process details coming soon.</p>
      </div>
    );
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>My Writing Process</h1>
      {stages.map((stage, index) => (
        <div key={stage.id} style={styles.step}>
          <div style={styles.number}>{index + 1}</div>
          <div style={styles.content}>
            <h3 style={styles.stepTitle}>{stage.title}</h3>
            <div style={styles.stepDesc} dangerouslySetInnerHTML={{ __html: stage.description }} />
          </div>
        </div>
      ))}
    </div>
  );
}
