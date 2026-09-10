'use client';

import { useState, useEffect } from 'react';
import { db } from '@/lib/firebase/client';
import { collection, getDocs, updateDoc, deleteDoc, doc } from 'firebase/firestore';

export default function AdminLeadsPage() {
  const [leads, setLeads] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadLeads();
  }, []);

  const loadLeads = async () => {
    try {
      const snap = await getDocs(collection(db, 'leads'));
      const list = snap.docs.map(d => ({ id: d.id, ...d.data() }));
      list.sort((a,b) => (a.createdAt || '').localeCompare(b.createdAt || ''));
      setLeads(list);
    } catch (err) {
      setError('Failed to load leads.');
    } finally {
      setLoading(false);
    }
  };

  const updateStatus = async (id, status) => {
    try {
      await updateDoc(doc(db, 'leads', id), { status });
      await loadLeads();
    } catch (err) {
      setError('Update failed.');
    }
  };

  const deleteLead = async (id) => {
    if (!confirm('Delete this lead?')) return;
    try {
      await deleteDoc(doc(db, 'leads', id));
      await loadLeads();
    } catch (err) {
      setError('Delete failed.');
    }
  };

  const styles = {
    container: { padding: '20px', maxWidth: '1000px', margin: '0 auto' },
    title: { color: '#C9A832', fontSize: '1.8rem', marginBottom: '20px' },
    table: { width: '100%', borderCollapse: 'collapse' },
    th: { textAlign: 'left', color: '#C9A832', padding: '10px', borderBottom: '1px solid #2D7D3A' },
    td: { padding: '10px', borderBottom: '1px solid #1A4D24', color: '#E8E8E8' },
    status: { padding: '4px 12px', borderRadius: '12px', fontSize: '0.8rem' },
    statusNew: { background: '#2D7D3A', color: '#C9A832' },
    statusContacted: { background: '#C9A832', color: '#0D2E17' },
    statusProgress: { background: '#4D1A1A', color: '#E8A0A0' },
    statusClosed: { background: '#6B8C6B', color: '#1A4D24' },
    buttonSmall: { padding: '4px 10px', borderRadius: '6px', border: '1px solid #C9A832', background: 'transparent', color: '#C9A832', cursor: 'pointer', margin: '2px' },
    buttonDanger: { padding: '4px 10px', borderRadius: '6px', border: '1px solid #E8A0A0', background: 'transparent', color: '#E8A0A0', cursor: 'pointer', margin: '2px' },
    error: { background: '#4D1A1A', padding: '12px', borderRadius: '8px', color: '#E8A0A0', border: '1px solid #C9A832', marginBottom: '16px' },
  };

  if (loading) return <p style={{ color: '#B8D9B8' }}>Loading...</p>;

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>📩 Leads</h1>
      {error && <div style={styles.error}>{error}</div>}
      {leads.length === 0 ? (
        <p style={{ color: '#B8D9B8' }}>No leads yet.</p>
      ) : (
        <table style={styles.table}>
          <thead><tr>
            <th style={styles.th}>Name</th>
            <th style={styles.th}>Email</th>
            <th style={styles.th}>Project</th>
            <th style={styles.th}>Status</th>
            <th style={styles.th}>Actions</th>
          </tr></thead>
          <tbody>
            {leads.map(lead => {
              const statusStyle = lead.status === 'new' ? styles.statusNew : lead.status === 'contacted' ? styles.statusContacted : lead.status === 'inprogress' ? styles.statusProgress : styles.statusClosed;
              return (
                <tr key={lead.id}>
                  <td style={styles.td}>{lead.name}</td>
                  <td style={styles.td}>{lead.email}</td>
                  <td style={styles.td}>{lead.projectType || '—'}</td>
                  <td style={styles.td}><span style={{ ...styles.status, ...statusStyle }}>{lead.status || 'new'}</span></td>
                  <td style={styles.td}>
                    <select onChange={(e) => updateStatus(lead.id, e.target.value)} defaultValue={lead.status || 'new'} style={{ background: '#1A4D24', color: '#E8E8E8', border: '1px solid #2D7D3A', borderRadius: '4px', padding: '4px' }}>
                      <option value="new">New</option>
                      <option value="contacted">Contacted</option>
                      <option value="inprogress">In Progress</option>
                      <option value="closed">Closed</option>
                    </select>
                    <button onClick={() => deleteLead(lead.id)} style={styles.buttonDanger}>🗑️</button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      )}
    </div>
  );
}
