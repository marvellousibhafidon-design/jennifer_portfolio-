'use client';

import { useState, useEffect } from 'react';
import { db } from '@/lib/firebase/client';
import { doc, getDoc, setDoc, collection, getDocs, query, where } from 'firebase/firestore';

export default function AdminHomepagePage() {
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);
  const [projects, setProjects] = useState([]);
  const [form, setForm] = useState({
    heroTitle: '',
    heroSubtext: '',
    heroCtaText: '',
    heroCtaLink: '/contact',
    heroImageUrl: '',
    heroImageAlt: '',
    trustBarText: '',
    featuredProjectIds: [],
  });

  useEffect(() => {
    const loadData = async () => {
      try {
        const docRef = doc(db, 'homepage', 'singleton');
        const docSnap = await getDoc(docRef);
        if (docSnap.exists()) setForm(docSnap.data());
        const q = query(collection(db, 'portfolio'), where('isPublished', '==', true));
        const snap = await getDocs(q);
        setProjects(snap.docs.map(d => ({ id: d.id, title: d.data().title })));
      } catch (err) {
        setError('Failed to load: ' + err.message);
      } finally {
        setLoading(false);
      }
    };
    loadData();
  }, []);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    if (type === 'checkbox') {
      setForm(prev => {
        const ids = prev.featuredProjectIds || [];
        if (checked) return { ...prev, featuredProjectIds: [...ids, value] };
        else return { ...prev, featuredProjectIds: ids.filter(id => id !== value) };
      });
    } else {
      setForm(prev => ({ ...prev, [name]: value }));
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSaving(true);
    setError(null);
    setSuccess(false);
    try {
      const docRef = doc(db, 'homepage', 'singleton');
      await setDoc(docRef, form, { merge: true });
      setSuccess(true);
      await fetch('/api/revalidate', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ path: '/' }) }).catch(() => {});
    } catch (err) {
      setError('Save failed: ' + err.message);
    } finally {
      setSaving(false);
    }
  };

  const styles = {
    container: { padding: '20px', maxWidth: '700px', margin: '0 auto' },
    title: { color: '#C9A832', fontSize: '1.8rem', marginBottom: '20px' },
    form: { display: 'flex', flexDirection: 'column', gap: '14px' },
    label: { color: '#C9A832', fontWeight: '600', display: 'block', marginBottom: '4px' },
    input: { width: '100%', padding: '10px', borderRadius: '8px', border: '1px solid #2D7D3A', background: '#0D2E17', color: '#E8E8E8', fontSize: '1rem' },
    textarea: { width: '100%', padding: '10px', borderRadius: '8px', border: '1px solid #2D7D3A', background: '#0D2E17', color: '#E8E8E8', fontSize: '1rem', minHeight: '80px' },
    checkboxGroup: { display: 'flex', flexDirection: 'column', gap: '6px', background: '#0D2E17', padding: '12px', borderRadius: '8px', border: '1px solid #2D7D3A' },
    checkboxLabel: { color: '#E8E8E8', display: 'flex', alignItems: 'center', gap: '8px' },
    button: { padding: '12px 24px', background: '#C9A832', color: '#0D2E17', border: 'none', borderRadius: '8px', fontWeight: '700', fontSize: '1rem', cursor: 'pointer' },
    buttonDisabled: { opacity: 0.6, cursor: 'not-allowed' },
    success: { background: '#2D7D3A', padding: '12px', borderRadius: '8px', color: '#C9A832', border: '1px solid #C9A832' },
    error: { background: '#4D1A1A', padding: '12px', borderRadius: '8px', color: '#E8A0A0', border: '1px solid #C9A832' },
  };

  if (loading) return <p style={{ color: '#B8D9B8' }}>Loading...</p>;

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>🏠 Homepage Editor</h1>
      {error && <div style={styles.error}>{error}</div>}
      {success && <div style={styles.success}>✅ Homepage updated!</div>}
      <form onSubmit={handleSubmit} style={styles.form}>
        <div><label style={styles.label}>Hero Title</label><input type="text" name="heroTitle" value={form.heroTitle || ''} onChange={handleChange} style={styles.input} placeholder="Your Ideas, Crafted into Writing" /></div>
        <div><label style={styles.label}>Hero Subtext</label><textarea name="heroSubtext" value={form.heroSubtext || ''} onChange={handleChange} style={styles.textarea} placeholder="Partner with me to bring your story to life." /></div>
        <div><label style={styles.label}>CTA Button Text</label><input type="text" name="heroCtaText" value={form.heroCtaText || ''} onChange={handleChange} style={styles.input} placeholder="Work With Me" /></div>
        <div><label style={styles.label}>CTA Link</label><input type="text" name="heroCtaLink" value={form.heroCtaLink || ''} onChange={handleChange} style={styles.input} placeholder="/contact" /></div>
        <div><label style={styles.label}>Hero Image URL</label><input type="text" name="heroImageUrl" value={form.heroImageUrl || ''} onChange={handleChange} style={styles.input} placeholder="https://example.com/hero.jpg" /></div>
        <div><label style={styles.label}>Trust Bar Text</label><input type="text" name="trustBarText" value={form.trustBarText || ''} onChange={handleChange} style={styles.input} placeholder="Trusted by authors & businesses worldwide" /></div>
        <div>
          <label style={styles.label}>Featured Projects</label>
          <div style={styles.checkboxGroup}>
            {projects.length === 0 ? <p style={{ color: '#B8D9B8' }}>No published projects yet.</p> :
              projects.map(p => (
                <label key={p.id} style={styles.checkboxLabel}>
                  <input type="checkbox" value={p.id} checked={(form.featuredProjectIds || []).includes(p.id)} onChange={handleChange} /> {p.title}
                </label>
              ))
            }
          </div>
        </div>
        <button type="submit" disabled={saving} style={{ ...styles.button, ...(saving ? styles.buttonDisabled : {}) }}>
          {saving ? 'Saving...' : 'Save Homepage'}
        </button>
      </form>
    </div>
  );
}
