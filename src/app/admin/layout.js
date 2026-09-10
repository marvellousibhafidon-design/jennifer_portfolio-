'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { usePathname, useRouter } from 'next/navigation';
import { auth } from '@/lib/firebase/client';

export default function AdminLayout({ children }) {
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const pathname = usePathname();
  const router = useRouter();

  const isLoginPage = pathname === '/admin';

  useEffect(() => {
    if (isLoginPage) {
      setLoading(false);
      return;
    }
    const unsubscribe = auth.onAuthStateChanged(async (user) => {
      if (user) {
        const token = await user.getIdTokenResult();
        if (token.claims.admin) {
          setUser(user);
        } else {
          router.push('/admin');
        }
      } else {
        router.push('/admin');
      }
      setLoading(false);
    });
    return () => unsubscribe();
  }, [router, isLoginPage]);

  const handleLogout = async () => {
    await auth.signOut();
    router.push('/admin');
  };

  const toggleSidebar = () => setSidebarOpen(!sidebarOpen);
  const toggleMobileMenu = () => setMobileMenuOpen(!mobileMenuOpen);

  const navItems = [
    { href: '/admin/dashboard', label: '📊 Dashboard' },
    { href: '/admin/homepage', label: '🏠 Homepage' },
    { href: '/admin/about', label: '👤 About' },
    { href: '/admin/services', label: '📋 Services' },
    { href: '/admin/portfolio', label: '📁 Portfolio' },
    { href: '/admin/testimonials', label: '⭐ Testimonials' },
    { href: '/admin/process', label: '🔄 Process' },
    { href: '/admin/leads', label: '📩 Leads' },
    { href: '/admin/settings', label: '⚙️ Settings' },
  ];

  if (isLoginPage) return <>{children}</>;

  if (loading) {
    return (
      <div style={{ minHeight: '100vh', background: '#1A4D24', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <p style={{ color: '#C9A832' }}>Loading...</p>
      </div>
    );
  }

  if (!user) return <>{children}</>;

  const styles = {
    container: { display: 'flex', minHeight: '100vh', background: '#1A4D24', fontFamily: 'Arial, sans-serif' },
    sidebar: { width: sidebarOpen ? '240px' : '0', background: '#0D2E17', borderRight: '2px solid #C9A832', padding: '20px', transition: 'width 0.3s', overflow: 'hidden', flexShrink: 0, position: 'sticky', top: 0, height: '100vh', overflowY: 'auto' },
    sidebarClosed: { width: '0', padding: '0', border: 'none' },
    sidebarTitle: { color: '#C9A832', fontSize: '1.2rem', fontWeight: '700', marginBottom: '30px', whiteSpace: 'nowrap' },
    navList: { listStyle: 'none', padding: 0, margin: 0 },
    navItem: { marginBottom: '8px' },
    navLink: { display: 'block', padding: '10px 16px', borderRadius: '8px', color: '#E8E8E8', textDecoration: 'none', transition: 'background 0.2s, color 0.2s' },
    navLinkActive: { background: '#2D7D3A', color: '#C9A832', fontWeight: '600' },
    main: { flex: 1, padding: '20px', overflowX: 'auto' },
    header: { display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '12px 16px', background: '#0D2E17', borderRadius: '8px', borderBottom: '2px solid #C9A832', marginBottom: '24px' },
    headerLeft: { display: 'flex', alignItems: 'center', gap: '12px' },
    hamburgerBtn: { background: 'none', border: 'none', color: '#C9A832', fontSize: '1.8rem', cursor: 'pointer', padding: '4px 8px' },
    userEmail: { color: '#B8D9B8', fontSize: '0.9rem' },
    logoutBtn: { background: 'transparent', border: '1px solid #C9A832', color: '#C9A832', padding: '6px 16px', borderRadius: '6px', cursor: 'pointer', transition: 'background 0.2s' },
    mobileMenu: { display: mobileMenuOpen ? 'block' : 'none', position: 'fixed', top: '60px', left: 0, right: 0, bottom: 0, background: '#0D2E17', padding: '20px', zIndex: 999, overflowY: 'auto', borderTop: '2px solid #C9A832' },
    mobileNavLink: { display: 'block', padding: '14px 16px', color: '#E8E8E8', textDecoration: 'none', borderBottom: '1px solid #1A4D24', fontSize: '1.1rem' },
    mobileNavLinkActive: { color: '#C9A832', fontWeight: '600', borderLeft: '4px solid #C9A832' },
  };

  return (
    <div style={styles.container}>
      <div style={{ ...styles.sidebar, ...(!sidebarOpen ? styles.sidebarClosed : {}) }}>
        <div style={styles.sidebarTitle}>📁 Admin</div>
        <ul style={styles.navList}>
          {navItems.map(item => {
            const isActive = pathname === item.href || pathname.startsWith(item.href + '/');
            return (
              <li key={item.href} style={styles.navItem}>
                <Link href={item.href} style={{ ...styles.navLink, ...(isActive ? styles.navLinkActive : {}) }}>
                  {item.label}
                </Link>
              </li>
            );
          })}
          <li style={styles.navItem}>
            <button onClick={handleLogout} style={{ ...styles.navLink, background: 'transparent', border: 'none', width: '100%', textAlign: 'left', cursor: 'pointer' }}>
              🚪 Logout
            </button>
          </li>
        </ul>
      </div>
      <div style={styles.main}>
        <div style={styles.header}>
          <div style={styles.headerLeft}>
            <button onClick={toggleSidebar} style={styles.hamburgerBtn} aria-label="Toggle sidebar">☰</button>
            <span style={{ color: '#C9A832', fontWeight: '600' }}>{pathname.split('/').pop() || 'Dashboard'}</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
            <Link href="/" style={{ color: '#C9A832', textDecoration: 'none', fontWeight: '500' }} target="_blank">🌐 View Site</Link>
            <span style={styles.userEmail}>{user?.email}</span>
            <button onClick={handleLogout} style={styles.logoutBtn}>Logout</button>
          </div>
        </div>
        {children}
      </div>
      <div style={styles.mobileMenu}>
        {navItems.map(item => {
          const isActive = pathname === item.href || pathname.startsWith(item.href + '/');
          return (
            <Link key={item.href} href={item.href} style={{ ...styles.mobileNavLink, ...(isActive ? styles.mobileNavLinkActive : {}) }} onClick={() => setMobileMenuOpen(false)}>
              {item.label}
            </Link>
          );
        })}
        <button onClick={() => { handleLogout(); setMobileMenuOpen(false); }} style={{ ...styles.mobileNavLink, background: 'none', border: 'none', width: '100%', textAlign: 'left', fontSize: '1.1rem', cursor: 'pointer' }}>
          🚪 Logout
        </button>
      </div>
    </div>
  );
}
