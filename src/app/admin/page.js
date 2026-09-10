'use client';

import { useState } from 'react';
import { auth } from '@/lib/firebase/client';
import { signInWithEmailAndPassword } from 'firebase/auth';
import { useRouter } from 'next/navigation';

export default function AdminLoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      const userCredential = await signInWithEmailAndPassword(auth, email, password);
      const idTokenResult = await userCredential.user.getIdTokenResult();
      if (idTokenResult.claims.admin) {
        router.push('/admin/dashboard');
      } else {
        setError('You do not have admin access.');
        await auth.signOut();
      }
    } catch {
      setError('Invalid email or password.');
    } finally {
      setLoading(false);
    }
  };

  const styles = {
    container: { minHeight: '100vh', display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#1A4D24', padding: '20px' },
    card: { background: '#0D2E17', padding: '40px', borderRadius: '16px', border: '2px solid #C9A832', maxWidth: '400px', width: '100%', boxShadow: '0 8px 32px rgba(0,0,0,0.5)' },
    title: { color: '#C9A832', fontSize: '1.8rem', fontWeight: '700', textAlign: 'center', marginBottom: '8px' },
    subtitle: { color: '#B8D9B8', fontSize: '0.95rem', textAlign: 'center', marginBottom: '30px' },
    label: { display: 'block', color: '#C9A832', fontWeight: '600', marginBottom: '6px' },
    input: { width: '100%', padding: '12px', border: '1px solid #C9A832', borderRadius: '8px', background: '#1A4D24', color: '#E8E8E8', fontSize: '1rem', boxSizing: 'border-box', marginBottom: '20px' },
    button: { width: '100%', padding: '14px', background: '#C9A832', color: '#0D2E17', border: 'none', borderRadius: '8px', fontSize: '1rem', fontWeight: '700', cursor: 'pointer' },
    buttonDisabled: { width: '100%', padding: '14px', background: '#6B8C6B', color: '#1A4D24', border: 'none', borderRadius: '8px', fontSize: '1rem', fontWeight: '700', cursor: 'not-allowed' },
    error: { color: '#E8A0A0', background: '#4D1A1A', padding: '12px', borderRadius: '8px', marginBottom: '16px', textAlign: 'center', border: '1px solid #C9A832' },
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h1 style={styles.title}>Admin Login</h1>
        <p style={styles.subtitle}>Jennifer Ibhafidon — Portfolio CMS</p>
        {error && <div style={styles.error}>{error}</div>}
        <form onSubmit={handleSubmit}>
          <label style={styles.label}>Email</label>
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} style={styles.input} required />
          <label style={styles.label}>Password</label>
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} style={styles.input} required />
          <button type="submit" disabled={loading} style={loading ? styles.buttonDisabled : styles.button}>
            {loading ? 'Logging in...' : 'Login'}
          </button>
        </form>
      </div>
    </div>
  );
}
