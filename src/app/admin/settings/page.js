'use client';

import { useState, useEffect } from 'react';
import { db } from '@/lib/firebase/client';
import { doc, getDoc, setDoc } from 'firebase/firestore';

export default function AdminSettingsPage() {
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);
  const [form, setForm] = useState({
    siteTitle: '',
    defaultMetaDescription: '',
    contactEmail: '',
    socialLinks: { linkedin: '', twitter: '' },
    logoUrl: '',
    faviconUrl: '',
  });

  useEffect(() => {
    const loadData = async () => {
      try {
        const docRef = doc(db, 'siteSettings', 'singleton');
        const docSnap = await getDoc(docRef);
        if (docSnap.exists()) setForm(docSnap.data());
      } catch (err) {
        setError('Failed to load: ' + err.message);
      } finally {
        setLoading(false);
      }
    };
    loadData();
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    if (name.startsWith('social.')) {
      const key = name.split('.')[1];
      setForm(prev => ({ ...prev, socialLinks: { ...prev.socialLinks, [key]: value } }));
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
      const docRef = doc(db, 'siteSettings', 'singleton');
      await setDoc(docRef, form, { merge: true });
      setSuccess(true);
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
    button: { padding: '12px 24px', background: '#C9A832', color: '#0D2E17', border: 'none', borderRadius: '8px', fontWeight: '700', fontSize: '1rem', cursor: 'pointer' },
    buttonDisabled: { opacity: 0.6, cursor: 'not-allowed' },
    success: { background: '#2D7D3A', padding: '12px', borderRadius: '8px', color: '#C9A832', border: '1px solid #C9A832' },
    error: { background: '#4D1A1A', padding: '12px', borderRadius: '8px', color: '#E8A0A0', border: '1px solid #C9A832' },
  };

  if (loading) return <p style={{ color: '#B8D9B8' }}>Loading...</p>;

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>⚙️ Settings</h1>
      {error && <div style={styles.error}>{error}</div>}
      {success && <div style={styles.success}>✅ Settings saved!</div>}
      <form onSubmit={handleSubmit} style={styles.form}>
        <div><label style={styles.label}>Site Title</label><input type="text" name="siteTitle" value={form.siteTitle || ''} onChange={handleChange} style={styles.input} /></div>
        <div><label style={styles.label}>Default Meta Description</label><input type="text" name="defaultMetaDescription" value={form.defaultMetaDescription || ''} onChange={handleChange} style={styles.input} /></div>
        <div><label style={styles.label}>Contact Email</label><input type="email" name="contactEmail" value={form.contactEmail || ''} onChange={handleChange} style={styles.input} /></div>
        <div><label style={styles.label}>LinkedIn URL</label><input type="text" name="social.linkedin" value={form.socialLinks?.linkedin || ''} onChange={handleChange} style={styles.input} /></div>
        <div><label style={styles.label}>Twitter URL</label><input type="text" name="social.twitter" value={form.socialLinks?.twitter || ''} onChange={handleChange} style={styles.input} /></div>
        <div><label style={styles.label}>Logo URL</label><input type="text" name="logoUrl" value={form.logoUrl || ''} onChange={handleChange} style={styles.input} /></div>
        <div><label style={styles.label}>Favicon URL</label><input type="text" name="faviconUrl" value={form.faviconUrl || ''} onChange={handleChange} style={styles.input} /></div>
        <button type="submit" disabled={saving} style={{ ...styles.button, ...(saving ? styles.buttonDisabled : {}) }}>
          {saving ? 'Saving...' : 'Save Settings'}
        </button>
      </form>
    </div>
  );
}
