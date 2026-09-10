'use client';

import { useState, useEffect } from 'react';
import { db } from '@/lib/firebase/client';
import { collection, getDocs, addDoc, updateDoc, deleteDoc, doc } from 'firebase/firestore';
import { slugify } from '@/lib/utils/slugify';
import { sanitizeHtml } from '@/lib/utils/sanitize';

export default function AdminPortfolioPage() {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [editingId, setEditingId] = useState(null);
  const [form, setForm] = useState({
    title: '',
    slug: '',
    category: '',
    excerpt: '',
    description: '',
    jenniferRole: '',
    year: '',
    clientName: '',
    visibility: 'public',
    coverImageUrl: '',
    coverImageAlt: '',
    galleryImages: [],
    isPublished: false,
    isFeatured: false,
    testimonialId: '',
    order: 0,
  });
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    loadProjects();
  }, []);

  const loadProjects = async () => {
    try {
      const snap = await getDocs(collection(db, 'portfolio'));
      const items = snap.docs.map(d => ({ id: d.id, ...d.data() }));
      items.sort((a, b) => (a.order || 0) - (b.order || 0));
      setProjects(items);
    } catch (err) {
      setError('Failed to load projects.');
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    if (type === 'checkbox') {
      setForm(prev => ({ ...prev, [name]: checked }));
    } else if (name === 'title') {
      setForm(prev => ({ ...prev, title: value, slug: slugify(value) }));
    } else {
      setForm(prev => ({ ...prev, [name]: value }));
    }
  };

  const resetForm = () => {
    setForm({
      title: '',
      slug: '',
      category: '',
      excerpt: '',
      description: '',
      jenniferRole: '',
      year: '',
      clientName: '',
      visibility: 'public',
      coverImageUrl: '',
      coverImageAlt: '',
      galleryImages: [],
      isPublished: false,
      isFeatured: false,
      testimonialId: '',
      order: projects.length,
    });
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
      const data = { ...form, description: sanitizeHtml(form.description), excerpt: sanitizeHtml(form.excerpt) };
      if (editingId) {
        await updateDoc(doc(db, 'portfolio', editingId), data);
      } else {
        await addDoc(collection(db, 'portfolio'), { ...data, order: projects.length });
      }
      setSuccess(true);
      await loadProjects();
      resetForm();
    } catch (err) {
      setError('Save failed: ' + err.message);
    } finally {
      setSubmitting(false);
    }
  };

  const handleEdit = (item) => {
    setEditingId(item.id);
    setForm(item);
  };

  const handleDelete = async (id) => {
    if (!confirm('Delete this project?')) return;
    try {
      await deleteDoc(doc(db, 'portfolio', id));
      await loadProjects();
    } catch (err) {
      setError('Delete failed: ' + err.message);
    }
  };

  const styles = {
    container: { padding: '20px', maxWidth: '1000px', margin: '0 auto' },
    title: { color: '#C9A832', fontSize: '1.8rem', marginBottom: '20px' },
    form: { background: '#0D2E17', padding: '20px', borderRadius: '12px', border: '1px solid #2D7D3A', marginBottom: '30px' },
    label: { color: '#C9A832', fontWeight: '600', display: 'block', marginBottom: '4px' },
    input: { width: '100%', padding: '10px', borderRadius: '8px', border: '1px solid #2D7D3A', background: '#1A4D24', color: '#E8E8E8', fontSize: '1rem', marginBottom: '12px' },
    textarea: { width: '100%', padding: '10px', borderRadius: '8px', border: '1px solid #2D7D3A', background: '#1A4D24', color: '#E8E8E8', fontSize: '1rem', minHeight: '80px', marginBottom: '12px' },
    select: { width: '100%', padding: '10px', borderRadius: '8px', border: '1px solid #2D7D3A', background: '#1A4D24', color: '#E8E8E8', fontSize: '1rem', marginBottom: '12px' },
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
      <h1 style={styles.title}>📁 Portfolio Manager</h1>
      {error && <div style={styles.error}>{error}</div>}
      {success && <div style={styles.success}>✅ Project saved!</div>}
      <div style={styles.form}>
        <h3 style={{ color: '#C9A832', marginBottom: '12px' }}>{editingId ? 'Edit Project' : 'Add New Project'}</h3>
        <form onSubmit={handleSubmit}>
          <label style={styles.label}>Title *</label>
          <input type="text" name="title" value={form.title} onChange={handleChange} style={styles.input} required />
          <label style={styles.label}>Slug (auto-generated)</label>
          <input type="text" name="slug" value={form.slug} onChange={handleChange} style={styles.input} />
          <label style={styles.label}>Category</label>
          <input type="text" name="category" value={form.category} onChange={handleChange} style={styles.input} />
          <label style={styles.label}>Excerpt (short summary)</label>
          <textarea name="excerpt" value={form.excerpt} onChange={handleChange} style={styles.textarea} />
          <label style={styles.label}>Description (full content)</label>
          <textarea name="description" value={form.description} onChange={handleChange} style={styles.textarea} />
          <label style={styles.label}>Your Role</label>
          <input type="text" name="jenniferRole" value={form.jenniferRole} onChange={handleChange} style={styles.input} />
          <label style={styles.label}>Year</label>
          <input type="number" name="year" value={form.year} onChange={handleChange} style={styles.input} />
          <label style={styles.label}>Client Name (optional)</label>
          <input type="text" name="clientName" value={form.clientName} onChange={handleChange} style={styles.input} />
          <label style={styles.label}>Visibility</label>
          <select name="visibility" value={form.visibility} onChange={handleChange} style={styles.select}>
            <option value="public">Public</option>
            <option value="anonymous">Anonymous</option>
          </select>
          <label style={styles.label}>Cover Image URL</label>
          <input type="text" name="coverImageUrl" value={form.coverImageUrl} onChange={handleChange} style={styles.input} />
          <label style={styles.label}>Cover Image Alt</label>
          <input type="text" name="coverImageAlt" value={form.coverImageAlt} onChange={handleChange} style={styles.input} />
          <label style={styles.label}>Gallery Images (comma separated URLs)</label>
          <input type="text" name="galleryImages" value={form.galleryImages.join(', ')} onChange={(e) => setForm(prev => ({ ...prev, galleryImages: e.target.value.split(',').map(s => s.trim()).filter(Boolean) }))} style={styles.input} placeholder="https://img1.jpg, https://img2.jpg" />
          <label style={styles.label}><input type="checkbox" name="isPublished" checked={form.isPublished} onChange={handleChange} style={styles.checkbox} /> Published</label>
          <label style={styles.label}><input type="checkbox" name="isFeatured" checked={form.isFeatured} onChange={handleChange} style={styles.checkbox} /> Featured</label>
          <button type="submit" disabled={submitting} style={styles.button}>{submitting ? 'Saving...' : 'Save'}</button>
          <button type="button" onClick={resetForm} style={{ ...styles.button, background: '#6B8C6B', marginLeft: '12px' }}>Cancel</button>
        </form>
      </div>
      <table style={styles.table}>
        <thead><tr><th style={styles.th}>Title</th><th style={styles.th}>Category</th><th style={styles.th}>Status</th><th style={styles.th}>Actions</th></tr></thead>
        <tbody>
          {projects.map(item => (
            <tr key={item.id}>
              <td style={styles.td}>{item.title}</td>
              <td style={styles.td}>{item.category}</td>
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
