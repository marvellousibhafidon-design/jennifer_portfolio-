'use client';

import { useEffect, useState } from 'react';
import { db, auth } from '@/lib/firebase/client';
import { collection, getDocs, query, where } from 'firebase/firestore';
import Link from 'next/link';

export default function AdminDashboardPage() {
  const [stats, setStats] = useState({ portfolio: 0, drafts: 0, services: 0, leads: 0 });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchStats = async () => {
    setLoading(true);
    setError(null);
    try {
      await auth.currentUser?.getIdToken(true);
      const portfolioSnap = await getDocs(collection(db, 'portfolio'));
      const allPortfolio = portfolioSnap.docs.length;
      const qPublished = query(collection(db, 'portfolio'), where('isPublished', '==', true));
      const publishedSnap = await getDocs(qPublished);
      const published = publishedSnap.docs.length;
      const servicesSnap = await getDocs(collection(db, 'services'));
      const leadsSnap = await getDocs(collection(db, 'leads'));
      setStats({
        portfolio: published,
        drafts: allPortfolio - published,
        services: servicesSnap.docs.length,
        leads: leadsSnap.docs.length,
      });
    } catch (err) {
      console.error('Error fetching stats:', err);
      setError(`Failed to load stats: ${err.message}. Please refresh token.`);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { fetchStats(); }, []);

  const handleRefreshToken = async () => {
    await auth.currentUser?.getIdToken(true);
    fetchStats();
  };

  const styles = {
    container: { padding: '10px 0' },
    grid: { display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(180px, 1fr))', gap: '20px', marginBottom: '30px' },
    card: { background: '#0D2E17', padding: '20px', borderRadius: '12px', border: '1px solid #2D7D3A', textAlign: 'center' },
    number: { fontSize: '2.5rem', fontWeight: '700', color: '#C9A832' },
    label: { fontSize: '0.9rem', color: '#B8D9B8' },
    quickLinks: { display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(160px, 1fr))', gap: '12px', marginTop: '10px' },
    link: { display: 'block', background: '#0D2E17', padding: '14px', borderRadius: '8px', border: '1px solid #2D7D3A', color: '#E8E8E8', textDecoration: 'none', textAlign: 'center', transition: 'border-color 0.3s' },
    error: { background: '#4D1A1A', padding: '16px', borderRadius: '8px', border: '1px solid #C9A832', color: '#E8A0A0', marginBottom: '20px' },
    btn: { background: '#C9A832', color: '#0D2E17', border: 'none', padding: '8px 20px', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold', marginLeft: '12px' },
  };

  if (loading) return <p style={{ color: '#B8D9B8' }}>Loading stats...</p>;

  if (error) {
    return (
      <div>
        <div style={styles.error}>
          <strong>⚠️ {error}</strong>
          <p style={{ marginTop: '8px', fontSize: '0.9rem' }}>Click the button below to refresh your admin token and retry.</p>
          <button onClick={handleRefreshToken} style={styles.btn}>Refresh Token & Retry</button>
        </div>
        <div style={styles.quickLinks}>
          <Link href="/admin/portfolio" style={styles.link}>📁 Manage Portfolio</Link>
          <Link href="/admin/services" style={styles.link}>📋 Manage Services</Link>
          <Link href="/admin/leads" style={styles.link}>📩 View Leads</Link>
        </div>
      </div>
    );
  }

  return (
    <div style={styles.container}>
      <div style={styles.grid}>
        <div style={styles.card}><div style={styles.number}>{stats.portfolio}</div><div style={styles.label}>Published Projects</div></div>
        <div style={styles.card}><div style={styles.number}>{stats.drafts}</div><div style={styles.label}>Drafts</div></div>
        <div style={styles.card}><div style={styles.number}>{stats.services}</div><div style={styles.label}>Services</div></div>
        <div style={styles.card}><div style={styles.number}>{stats.leads}</div><div style={styles.label}>New Leads</div></div>
      </div>
      <h2 style={{ color: '#C9A832', fontSize: '1.3rem', marginBottom: '16px' }}>Quick Actions</h2>
      <div style={styles.quickLinks}>
        <Link href="/admin/portfolio/new" style={styles.link}>➕ Add Project</Link>
        <Link href="/admin/services/new" style={styles.link}>➕ Add Service</Link>
        <Link href="/admin/testimonials/new" style={styles.link}>➕ Add Testimonial</Link>
        <Link href="/admin/leads" style={styles.link}>📩 View Leads</Link>
      </div>
    </div>
  );
}
