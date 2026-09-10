'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';

export default function PublicLayout({ children }) {
  const [menuOpen, setMenuOpen] = useState(false);
  const [showBackToTop, setShowBackToTop] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setShowBackToTop(window.scrollY > 400);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const styles = {
    body: {
      margin: 0,
      padding: 0,
      background: '#1A4D24',
      minHeight: '100vh',
      fontFamily: '"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
      color: '#E8E8E8',
    },
    nav: {
      background: '#0D2E17',
      padding: '16px 24px',
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      borderBottom: '3px solid #C9A832',
      position: 'sticky',
      top: 0,
      zIndex: 1000,
      boxShadow: '0 4px 20px rgba(0,0,0,0.4)',
    },
    logo: {
      color: '#C9A832',
      fontSize: '1.6rem',
      fontWeight: '700',
      textDecoration: 'none',
      letterSpacing: '-0.5px',
    },
    logoSpan: {
      color: '#E8E8E8',
      fontWeight: '300',
    },
    hamburger: {
      display: 'none',
      flexDirection: 'column',
      cursor: 'pointer',
      gap: '5px',
      background: 'none',
      border: 'none',
      padding: '5px',
    },
    hamburgerLine: {
      width: '30px',
      height: '3px',
      background: '#C9A832',
      borderRadius: '2px',
      transition: 'all 0.3s',
    },
    navLinks: {
      display: 'flex',
      gap: '32px',
      listStyle: 'none',
      margin: 0,
      padding: 0,
      alignItems: 'center',
    },
    navLink: {
      color: '#E8E8E8',
      textDecoration: 'none',
      fontSize: '1rem',
      fontWeight: '500',
      transition: 'color 0.3s, border-bottom 0.3s',
      paddingBottom: '4px',
      borderBottom: '2px solid transparent',
    },
    mobileMenu: {
      display: 'none',
      flexDirection: 'column',
      background: '#0D2E17',
      padding: '20px 24px',
      gap: '12px',
      borderBottom: '2px solid #C9A832',
    },
    mobileLink: {
      color: '#E8E8E8',
      textDecoration: 'none',
      fontSize: '1.1rem',
      padding: '12px 0',
      borderBottom: '1px solid #1A4D24',
      textAlign: 'center',
      transition: 'color 0.3s',
    },
    footer: {
      background: '#0D2E17',
      padding: '40px 24px 20px',
      borderTop: '3px solid #C9A832',
      textAlign: 'center',
      marginTop: '40px',
    },
    footerContainer: {
      maxWidth: '1200px',
      margin: '0 auto',
    },
    footerSocial: {
      display: 'flex',
      justifyContent: 'center',
      gap: '20px',
      marginBottom: '20px',
    },
    footerSocialLink: {
      color: '#C9A832',
      textDecoration: 'none',
      fontSize: '1.2rem',
      transition: 'color 0.3s, transform 0.3s',
      display: 'inline-block',
    },
    footerText: {
      color: '#B8D9B8',
      fontSize: '0.9rem',
      margin: '4px 0',
    },
    footerGold: {
      color: '#C9A832',
    },
    backToTop: {
      position: 'fixed',
      bottom: '30px',
      right: '30px',
      background: '#C9A832',
      color: '#0D2E17',
      border: 'none',
      borderRadius: '50%',
      width: '50px',
      height: '50px',
      fontSize: '1.5rem',
      cursor: 'pointer',
      boxShadow: '0 4px 15px rgba(201,168,50,0.4)',
      transition: 'transform 0.3s, opacity 0.3s',
      opacity: showBackToTop ? 1 : 0,
      pointerEvents: showBackToTop ? 'auto' : 'none',
      zIndex: 999,
    },
    container: {
      maxWidth: '1200px',
      margin: '0 auto',
      padding: '0 20px',
      animation: 'fadeIn 0.6s ease-in',
    },
  };

  return (
    <>
      <style>{`
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(20px); }
          to { opacity: 1; transform: translateY(0); }
        }
        @media (min-width: 769px) {
          button[aria-label="Toggle menu"] { display: none !important; }
          ul { display: flex !important; }
        }
        @media (max-width: 768px) {
          ul { display: none !important; }
          button[aria-label="Toggle menu"] { display: flex !important; }
        }
      `}</style>

      <nav style={styles.nav}>
        <Link href="/" style={styles.logo}>
          Jennifer <span style={styles.logoSpan}>Ibhafidon</span>
        </Link>
        <button onClick={() => setMenuOpen(!menuOpen)} style={styles.hamburger} aria-label="Toggle menu">
          <span style={{ ...styles.hamburgerLine, transform: menuOpen ? 'rotate(45deg) translate(5px, 5px)' : 'none' }} />
          <span style={{ ...styles.hamburgerLine, opacity: menuOpen ? 0 : 1 }} />
          <span style={{ ...styles.hamburgerLine, transform: menuOpen ? 'rotate(-45deg) translate(5px, -5px)' : 'none' }} />
        </button>
        <ul style={styles.navLinks}>
          <li><Link href="/" style={styles.navLink}>Home</Link></li>
          <li><Link href="/about" style={styles.navLink}>About</Link></li>
          <li><Link href="/services" style={styles.navLink}>Services</Link></li>
          <li><Link href="/contact" style={styles.navLink}>Contact</Link></li>
        </ul>
      </nav>

      <div style={{ ...styles.mobileMenu, display: menuOpen ? 'flex' : 'none' }}>
        <Link href="/" style={styles.mobileLink} onClick={() => setMenuOpen(false)}>Home</Link>
        <Link href="/about" style={styles.mobileLink} onClick={() => setMenuOpen(false)}>About</Link>
        <Link href="/services" style={styles.mobileLink} onClick={() => setMenuOpen(false)}>Services</Link>
        <Link href="/contact" style={styles.mobileLink} onClick={() => setMenuOpen(false)}>Contact</Link>
      </div>

      <div style={styles.container}>{children}</div>

      <footer style={styles.footer}>
        <div style={styles.footerContainer}>
          <div style={styles.footerSocial}>
            <a href="#" style={styles.footerSocialLink}>LinkedIn</a>
            <a href="#" style={styles.footerSocialLink}>Twitter</a>
            <a href="mailto:ibhafidonjennifer4@gmail.com" style={styles.footerSocialLink}>Email</a>
          </div>
          <p style={styles.footerText}>
            © {new Date().getFullYear()} <span style={styles.footerGold}>Jennifer Ibhafidon</span>. All rights reserved.
          </p>
          <p style={{ fontSize: '0.8rem', color: '#6B8C6B' }}>Ghostwriter &amp; Editorial Partner</p>
        </div>
      </footer>

      <button onClick={scrollToTop} style={styles.backToTop} aria-label="Back to top">↑</button>
    </>
  );
}
