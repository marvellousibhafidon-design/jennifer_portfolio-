'use client';

import { useState } from 'react';

export default function ContactPage() {
  const [formData, setFormData] = useState({ name: '', email: '', projectType: '', description: '', timeline: '' });
  const [status, setStatus] = useState(null);
  const [loading, setLoading] = useState(false);

  const styles = {
    container: { maxWidth: '700px', margin: '0 auto', padding: '40px 20px' },
    title: { fontSize: '2.5rem', color: '#C9A832', marginBottom: '10px' },
    sub: { fontSize: '1.1rem', color: '#B8D9B8', marginBottom: '30px' },
    label: { display: 'block', fontWeight: 'bold', marginBottom: '6px', color: '#C9A832' },
    input: { width: '100%', padding: '12px', border: '1px solid #C9A832', borderRadius: '8px', fontSize: '1rem', marginBottom: '20px', boxSizing: 'border-box', background: '#0D2E17', color: '#E8E8E8' },
    textarea: { width: '100%', padding: '12px', border: '1px solid #C9A832', borderRadius: '8px', fontSize: '1rem', marginBottom: '20px', boxSizing: 'border-box', minHeight: '150px', background: '#0D2E17', color: '#E8E8E8' },
    select: { width: '100%', padding: '12px', border: '1px solid #C9A832', borderRadius: '8px', fontSize: '1rem', marginBottom: '20px', boxSizing: 'border-box', background: '#0D2E17', color: '#E8E8E8' },
    btn: { padding: '14px 40px', background: '#C9A832', color: '#0D2E17', border: 'none', borderRadius: '50px', fontWeight: 'bold', fontSize: '1rem', cursor: 'pointer' },
    btnDisabled: { padding: '14px 40px', background: '#6B8C6B', color: '#1A4D24', border: 'none', borderRadius: '50px', fontWeight: 'bold', fontSize: '1rem', cursor: 'not-allowed' },
    success: { background: '#2D7D3A', color: '#C9A832', padding: '16px', borderRadius: '8px', marginBottom: '20px', border: '1px solid #C9A832' },
    error: { background: '#4D1A1A', color: '#E8A0A0', padding: '16px', borderRadius: '8px', marginBottom: '20px', border: '1px solid #C9A832' },
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setStatus(null);
    try {
      const res = await fetch('/api/leads', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });
      if (res.ok) {
        setStatus('success');
        setFormData({ name: '', email: '', projectType: '', description: '', timeline: '' });
      } else {
        setStatus('error');
      }
    } catch {
      setStatus('error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Work With Me</h1>
      <p style={styles.sub}>Have a project in mind? Let&apos;s talk.</p>
      <form onSubmit={handleSubmit}>
        <label style={styles.label}>Name *</label>
        <input type="text" required style={styles.input} value={formData.name} onChange={(e) => setFormData({ ...formData, name: e.target.value })} />
        <label style={styles.label}>Email *</label>
        <input type="email" required style={styles.input} value={formData.email} onChange={(e) => setFormData({ ...formData, email: e.target.value })} />
        <label style={styles.label}>Project Type</label>
        <select style={styles.select} value={formData.projectType} onChange={(e) => setFormData({ ...formData, projectType: e.target.value })}>
          <option value="">Select...</option>
          <option value="book">Book / eBook</option>
          <option value="article">Article / Blog</option>
          <option value="linkedin">LinkedIn / Thought Leadership</option>
          <option value="newsletter">Newsletter</option>
          <option value="other">Other</option>
        </select>
        <label style={styles.label}>Description *</label>
        <textarea required style={styles.textarea} value={formData.description} onChange={(e) => setFormData({ ...formData, description: e.target.value })} />
        <label style={styles.label}>Timeline</label>
        <input type="text" placeholder="e.g., 3 months" style={styles.input} value={formData.timeline} onChange={(e) => setFormData({ ...formData, timeline: e.target.value })} />
        <button type="submit" disabled={loading} style={loading ? styles.btnDisabled : styles.btn}>
          {loading ? 'Sending...' : 'Send Message'}
        </button>
      </form>
      {status === 'success' && <div style={styles.success}>✅ Thank you! I'll be in touch soon.</div>}
      {status === 'error' && <div style={styles.error}>❌ Something went wrong. Please try again.</div>}
    </div>
  );
}
