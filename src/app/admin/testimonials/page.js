'use client';

import { useState, useEffect } from 'react';
import { db } from '@/lib/firebase/client';
import { collection, getDocs, addDoc, updateDoc, deleteDoc, doc } from 'firebase/firestore';

export default function AdminTestimonialsPage() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [editingId, setEditingId] = useState(null);
  const [form, setForm] = useState({ clientName: '', clientRole: '', clientCompany: '', quote: '', photoUrl: '', isPublished: false, order: 0 });
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => { loadItems(); }, []);

  const loadItems = async () => {
    try {
      const snap = await getDocs(collection(db, 'testimonials'));
      const list = snap.docs.map(d => ({ id: d.id, ...d.data() }));
      list.sort((a,b) => a.order - b.order);
      setItems(list);
    } catch { setError('Failed to load.'); } finally { setLoading(false); }
  };

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setForm(prev => ({ ...prev, [name]: type === 'checkbox' ? checked : value }));
  };

  const resetForm = () => {
    setForm({ clientName: '', clientRole: '', clientCompany: '', quote: '', photoUrl: '', isPublished: false, order: items.length });
    setEditingId(null);
    setError(null);
    setSuccess(false);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitting(true);
    setError(null);
    setSuccess(false);
    try {
      if (editingId) await updateDoc(doc(db, 'testimonials', editingId), form);
      else await addDoc(collection(db, 'testimonials'), { ...form, order: items.length });
      setSuccess(true);
      await loadItems();
      resetForm();
    } catch (err) {
      setError('Save failed: ' + err.message);
    } finally {
      setSubmitting(false);
    }
  };

  const handleEdit = (item) => { setEditingId(item.id); setForm(item); };
  const handleDelete = async (id) => { if (!confirm('Delete?')) return; await deleteDoc(doc(db, 'testimonials', id)); await loadItems(); };

  const styles = {
    container: { padding: '20px', maxWidth: '800px', margin: '0 auto' },
    title: { color: '#C9A832', fontSize: '1.8rem', marginBottom: '20px' },
    form: { background: '#0D2E17', padding: '20px', borderRadius: '12px', border: '1px solid #2D7D3A', marginBottom: '30px' },
    label: { color: '#C9A832', fontWeight: '600', display: 'block', marginBottom: '4px' },
    input: { width: '100%', padding: '10px', borderRadius: '8px', border: '1px solid #2D7D3A', background: '#1A4D24', color: '#E8E8E8', fontSize: '1rem', marginBottom: '12px' },
    textarea: { width: '100%', padding: '10px', borderRadius: '8px', border: '1px solid #2D7D3A', background: '#1A4D24', color: '#E8E8E8', fontSize: '1rem', minHeight: '80px', marginBottom: '12px' },
    checkbox: { marginRight: '8px' },
    button: { padding: '10px 20px', background: '#C9A832', color: '#0D2E17', border: 'none', borderRadius: '8px', fontWeight: '700', cursor: 'pointer' },
    buttonDanger: { padding: '6px 12px', background: '#4D1A1A', color: '#E8A0A0', border: '1px solid #C9A832', borderRadius: '6px', cursor: 'pointer' },
    buttonSmall: { padding: '6px 12px', background: '#2D7D3A', color: '#E8E8E8', border: 'none', borderRadius: '6px', cursor: 'pointer', marginRight: '8px' },
    table: { width: '100%', borderCollapse: 'collapse' },
    th: { textAlign: 'left', color: '#C9A832', padding: '10px', borderBottom: '1px solid #2D7D3A' },
    td: { padding: '10px', borderBottom: '1px solid #1A4D24', color: '#E8E8E8' },
    success: { background: '#2D7D3A', padding: '10px', borderRadius: '8px', color: '#C9A832', border: '1px solid #C9A832', marginBottom: '12px' },
    error: { background: '#4D1A1A', padding: '10px', borderRadius: '8px', color: '#E8A0A0', border: '1px solid #C9A832', marginBottom: '12px' },
  };

  if (loading) return <p style={{ color: '#B8D9B8' }}>Loading...</p>;

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>⭐ Testimonials</h1>
      {error && <div style={styles.error}>{error}</div>}
      {success && <div style={styles.success}>✅ Saved!</div>}
      <div style={styles.form}>
        <h3 style={{ color: '#C9A832', marginBottom: '12px' }}>{editingId ? 'Edit' : 'Add'} Testimonial</h3>
        <form onSubmit={handleSubmit}>
          <label style={styles.label}>Client Name *</label>
          <input type="text" name="clientName" value={form.clientName} onChange={handleChange} style={styles.input} required />
          <label style={styles.label}>Role</label>
          <input type="text" name="clientRole" value={form.clientRole} onChange={handleChange} style={styles.input} />
          <label style={styles.label}>Company</label>
          <input type="text" name="clientCompany" value={form.clientCompany} onChange={handleChange} style={styles.input} />
          <label style={styles.label}>Quote *</label>
          <textarea name="quote" value={form.quote} onChange={handleChange} style={styles.textarea} required />
          <label style={styles.label}>Photo URL</label>
          <input type="text" name="photoUrl" value={form.photoUrl} onChange={handleChange} style={styles.input} />
          <label style={styles.label}><input type="checkbox" name="isPublished" checked={form.isPublished} onChange={handleChange} style={styles.checkbox} /> Published</label>
          <button type="submit" disabled={submitting} style={styles.button}>{submitting ? 'Saving...' : 'Save'}</button>
          <button type="button" onClick={resetForm} style={{ ...styles.button, background: '#6B8C6B', marginLeft: '12px' }}>Cancel</button>
        </form>
      </div>
      <table style={styles.table}>
        <thead><tr><th style={styles.th}>Client</th><th style={styles.th}>Status</th><th style={styles.th}>Actions</th></tr></thead>
        <tbody>
          {items.map(item => (
            <tr key={item.id}>
              <td style={styles.td}>{item.clientName}</td>
              <td style={styles.td}>{item.isPublished ? '✅ Published' : '📄 Draft'}</td>
              <td style={styles.td}>
                <button onClick={() => handleEdit(item)} style={styles.buttonSmall}>✏️ Edit</button>
                <button onClick={() => handleDelete(item.id)} style={styles.buttonDanger}>🗑️ Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
