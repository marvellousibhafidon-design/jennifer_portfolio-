'use client';

import { useState, useEffect } from 'react';
import { db } from '@/lib/firebase/client';
import { doc, getDoc, setDoc } from 'firebase/firestore';

export default function AdminAboutPage() {
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);
  const [form, setForm] = useState({
    biography: '',
    philosophy: '',
    specialties: [],
    profileImageUrl: '',
    profileImageAlt: '',
  });

  useEffect(() => {
    const loadData = async () => {
      try {
        const docRef = doc(db, 'about', 'singleton');
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
    if (name === 'specialties') {
      const items = value.split(',').map(s => s.trim()).filter(Boolean);
      setForm(prev => ({ ...prev, specialties: items }));
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
      const docRef = doc(db, 'about', 'singleton');
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
    textarea: { width: '100%', padding: '10px', borderRadius: '8px', border: '1px solid #2D7D3A', background: '#0D2E17', color: '#E8E8E8', fontSize: '1rem', minHeight: '120px' },
    button: { padding: '12px 24px', background: '#C9A832', color: '#0D2E17', border: 'none', borderRadius: '8px', fontWeight: '700', fontSize: '1rem', cursor: 'pointer' },
    buttonDisabled: { opacity: 0.6, cursor: 'not-allowed' },
    success: { background: '#2D7D3A', padding: '12px', borderRadius: '8px', color: '#C9A832', border: '1px solid #C9A832' },
    error: { background: '#4D1A1A', padding: '12px', borderRadius: '8px', color: '#E8A0A0', border: '1px solid #C9A832' },
  };

  if (loading) return <p style={{ color: '#B8D9B8' }}>Loading...</p>;

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>👤 About Editor</h1>
      {error && <div style={styles.error}>{error}</div>}
      {success && <div style={styles.success}>✅ About updated!</div>}
      <form onSubmit={handleSubmit} style={styles.form}>
        <div><label style={styles.label}>Biography</label><textarea name="biography" value={form.biography || ''} onChange={handleChange} style={styles.textarea} placeholder="Write the biography..." /></div>
        <div><label style={styles.label}>Philosophy</label><textarea name="philosophy" value={form.philosophy || ''} onChange={handleChange} style={styles.textarea} placeholder="Writing philosophy..." /></div>
        <div><label style={styles.label}>Specialties (comma separated)</label><input type="text" name="specialties" value={(form.specialties || []).join(', ')} onChange={handleChange} style={styles.input} placeholder="Fiction, Non-fiction, Business Writing" /></div>
        <div><label style={styles.label}>Profile Image URL</label><input type="text" name="profileImageUrl" value={form.profileImageUrl || ''} onChange={handleChange} style={styles.input} placeholder="https://example.com/photo.jpg" /></div>
        <div><label style={styles.label}>Profile Image Alt</label><input type="text" name="profileImageAlt" value={form.profileImageAlt || ''} onChange={handleChange} style={styles.input} placeholder="Jennifer Ibhafidon" /></div>
        <button type="submit" disabled={saving} style={{ ...styles.button, ...(saving ? styles.buttonDisabled : {}) }}>
          {saving ? 'Saving...' : 'Save About'}
        </button>
      </form>
    </div>
  );
}
