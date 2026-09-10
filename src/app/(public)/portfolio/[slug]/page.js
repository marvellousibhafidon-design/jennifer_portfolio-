import { db } from '@/lib/firebase/admin';
import { notFound } from 'next/navigation';

export const revalidate = 3600;

export async function generateStaticParams() {
  const snapshot = await db.collection('portfolio')
    .where('isPublished', '==', true)
    .get();
  return snapshot.docs.map(doc => ({ slug: doc.data().slug }));
}

async function getProject(slug) {
  const snapshot = await db.collection('portfolio')
    .where('slug', '==', slug)
    .where('isPublished', '==', true)
    .limit(1)
    .get();
  if (snapshot.empty) return null;
  const doc = snapshot.docs[0];
  const data = doc.data();
  let testimonial = null;
  if (data.testimonialId) {
    const tDoc = await db.collection('testimonials').doc(data.testimonialId).get();
    if (tDoc.exists && tDoc.data().isPublished) {
      testimonial = { id: tDoc.id, ...tDoc.data() };
    }
  }
  return { id: doc.id, ...data, testimonial };
}

export async function generateMetadata({ params }) {
  const project = await getProject(params.slug);
  if (!project) return { title: 'Not Found' };
  return {
    title: project.metaTitle || `${project.title} | Jennifer Ibhafidon`,
    description: project.metaDescription || project.excerpt || project.description?.slice(0, 160),
    openGraph: {
      title: project.metaTitle || project.title,
      description: project.metaDescription || project.excerpt,
      images: project.coverImageUrl ? [{ url: project.coverImageUrl }] : [],
    },
  };
}

export default async function PortfolioDetailPage({ params }) {
  const project = await getProject(params.slug);
  if (!project) notFound();

  const showClient = project.visibility === 'public' && project.clientName;

  const styles = {
    container: { maxWidth: '900px', margin: '0 auto', padding: '40px 20px' },
    image: { width: '100%', maxHeight: '400px', objectFit: 'cover', borderRadius: '12px', marginBottom: '20px', border: '2px solid #C9A832' },
    title: { fontSize: '2.5rem', color: '#C9A832', marginBottom: '10px' },
    meta: { color: '#B8D9B8', marginBottom: '20px' },
    body: { fontSize: '1.1rem', lineHeight: '1.8', color: '#E8E8E8' },
    gallery: { display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))', gap: '16px', marginTop: '30px' },
    galleryImg: { width: '100%', height: '150px', objectFit: 'cover', borderRadius: '8px', border: '1px solid #3A8F48' },
    testimonial: { background: '#0D2E17', padding: '20px', borderRadius: '12px', marginTop: '30px', border: '1px solid #C9A832' },
    testimonialQuote: { fontSize: '1.2rem', color: '#E8E8E8', fontStyle: 'italic' },
    testimonialCite: { color: '#C9A832', marginTop: '10px', display: 'block' },
  };

  return (
    <div style={styles.container}>
      {project.coverImageUrl && <img src={project.coverImageUrl} alt={project.title} style={styles.image} />}
      <h1 style={styles.title}>{project.title}</h1>
      <div style={styles.meta}>
        {project.category && <span>Category: {project.category}</span>}
        {project.year && <span style={{ marginLeft: '16px' }}>Year: {project.year}</span>}
        {project.jenniferRole && <span style={{ marginLeft: '16px' }}>Role: {project.jenniferRole}</span>}
        {showClient && <span style={{ marginLeft: '16px' }}>Client: {project.clientName}</span>}
      </div>
      <div style={styles.body} dangerouslySetInnerHTML={{ __html: project.description }} />
      {project.galleryImages?.length > 0 && (
        <div style={styles.gallery}>
          {project.galleryImages.map((url, i) => <img key={i} src={url} alt={`${project.title} ${i+1}`} style={styles.galleryImg} />)}
        </div>
      )}
      {project.testimonial && (
        <div style={styles.testimonial}>
          <p style={styles.testimonialQuote}>"{project.testimonial.quote}"</p>
          <cite style={styles.testimonialCite}>
            {project.testimonial.clientName}
            {project.testimonial.clientRole && `, ${project.testimonial.clientRole}`}
          </cite>
        </div>
      )}
    </div>
  );
}
