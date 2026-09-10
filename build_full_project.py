import os
import json

def create_file(path, content):
    dirname = os.path.dirname(path)
    if dirname:  # only create directory if there is one
        os.makedirs(dirname, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ {path}")
def main():
    print("🚀 Building full Jennifer Ibhafidon portfolio project...\n")

    # -------------------------------------------------------------
    # ROOT FILES
    # -------------------------------------------------------------
    create_file(".env.example", """# Public (safe for client)
NEXT_PUBLIC_FIREBASE_API_KEY=AIzaSyDyzlOnj9ADABMvW01VXCnK2qMHOnLoeKo
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=jennifer-portfolio-b9717.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=jennifer-portfolio-b9717
NEXT_PUBLIC_FIREBASE_APP_ID=1:397089218927:web:a355d823255e39bf9bc89a

# Server-Only (NEVER use NEXT_PUBLIC_ prefix)
FIREBASE_PROJECT_ID=jennifer-portfolio-b9717
FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC9lndsETqDjKTy\\nMxelia717X2Fft9SJhXW5iQFSGLFXo9s+nPWIDm6/JOsYrDp/gXpKjGAut3LHJJ/\\nOXCAnk/CdJXq+8udnyYMSsOW+fPrxalM/+K+vJrjBqGFF+X2PEPjwqUK5lBBKCtw\\nZlhTKARU60ItTOwokAohOC1GlUh77cQYhuXGN5SkqzZprwp/9rCXtWY/APwWmS1X\\nCZvpp7it1rJIoInyV01sX0euU3NUGeaGmJ+trCyhxZuCfBpMg7IVql95J+hxGMLR\\ntX00CZSzEcSKusq717GUsc/uLUJLXbzMqq/MuVS3gOyaQi4FqnDJbuog7WeHGLOg\\nWp8O1YF7AgMBAAECggEAKxDN6d90AkPliBrxCSpgcv7Sn4t1YSzDk0BN+GE8Bod3\\nXxL5Uy+YzY/oX6U/eLe6Uf/CpPJNxYClCn9avey4Q3zGPU2bMB/hvbMSAO6gaPNK\\nhPIvaJJhQKbV8+y80RVZephRc0tj+ZkNXQfyklkpuryCGNY7Yu9tTaR8LGdmwreY\\nli+2dxhnkpNBUxC9rUbnHv2WzHSX0iqpn5cW2sP7XrT5motw6Sth/ZlOf+fBHHj7\\nLmxR+0SITPCgkXn2z3bZz2sYpI/QkMHGOOPXB4GesXWwKUrj+PgdT5a64uYe2z7J\\nO26JYi6IRbtDqZ6uw0/aVCm3Awvmsq4GOYZinEBm6QKBgQDstU4VstMhv7uiDr4L\\nuNVTadlGL8tBjdtfMdMgyE5J+HsdF3CndlypmGof4peKw9S0gqrmmwQkSJhZgTTQ\\nJva7o6rNW3sPPMCufPE9ZNJ1KFT+KepL/HiSHtb8vR7i1NSRPzd6l0BtncMjX5zC\\ngEOGRnQxzK9C7+zk4gP/l6njLwKBgQDNCgmHegWIC8SS0btQJmeRu4tgHVI8NwRH\\naKB869ICjLMxL+5TLYH4rKRZSGtcceZzQDW71NPAt88MWd08VKyQiTKXQ3KIrpYJ\\nqHWhKx4vbgwtJKB2Jt/DT5wVw7j2qbwu3h8WT+eAPtdvnyKIdmEO7tVQtXRVJIL1\\nqpHGiqLjdQKBgF9jaMYhvCd7hnd2DWvX3k+w9hfsprISIncoMvahAbuZYLOGgKVb\\nc1f8zbdvrrYC2LKtfYVUrsSYZJydDtVa/k77U5dR6DNpvhQS0Xx2JsGDsUyDQ6G/\\nai8oMmbDJ7EtJ0Qo/4htb089JigZHajb21o/BhATdgU5fnN2CTp0uceNAoGAcq0A\\nc2MNoO9j+/GNX+B64IkSBKmhisgCfqXHzNZf2Mk0l3gFRUQYgyqbqMvWMBgMGb15\\n0BnSbODgzjmcgNeixBvXzb4NWuC6TaCIWaGx+jkEWmM3050eXTAzTgDvfBWmiFf2\\n7xW1loaPG4DXYZdD5YQyjjdOXyhSjm/dpDt5qtkCgYEAzxrhu1qaNcHYth+ni383\\nTFEF6u9WMaoM72bUwI+iKaE/RCGT7m/tKu9dDRqw/XRkIXLqMcPSFJUoeWeOpN3a\\nq0l2DKvpfIAsO69gf554RnojUhNRadwXwCsLvNeE0hkLIJzldZk+9F92rKsjixxz\\nS7IXSpicfsq5HPXxeXHrXoo=\\n-----END PRIVATE KEY-----\\n"
FIREBASE_CLIENT_EMAIL=firebase-adminsdk-fbsvc@jennifer-portfolio-b9717.iam.gserviceaccount.com
REVALIDATE_SECRET=supersecret
""")

    create_file(".gitignore", """# dependencies
node_modules/
.next/
out/

# environment
.env
.env.local
.env.*.local

# build
dist/
build/

# logs
*.log
npm-debug.log*

# OS
.DS_Store
Thumbs.db

# Firebase
firebase-debug.log
.firebase/

# Netlify
.netlify/
""")

    create_file("package.json", json.dumps({
        "name": "jennifer-ibhafidon-portfolio",
        "version": "0.1.0",
        "private": True,
        "scripts": {
            "dev": "next dev",
            "build": "next build",
            "start": "next start",
            "lint": "next lint",
            "grant-admin": "node scripts/grant-admin.js"
        },
        "dependencies": {
            "next": "latest",
            "react": "latest",
            "react-dom": "latest",
            "firebase": "latest",
            "firebase-admin": "latest",
            "@netlify/blobs": "latest",
            "dompurify": "latest",
            "jsdom": "latest"
        },
        "devDependencies": {
            "@types/node": "latest",
            "@types/react": "latest",
            "@types/react-dom": "latest",
            "typescript": "latest",
            "dotenv": "latest"
        }
    }, indent=2))

    create_file("next.config.js", """/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    serverActions: {
      allowedOrigins: ['localhost:3000'],
    },
  },
  images: {
    remotePatterns: [],
  },
};
module.exports = nextConfig;
""")

    create_file("jsconfig.json", """{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
""")

    create_file("firestore.rules", """rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    function isAdmin() {
      return request.auth != null && request.auth.token.admin == true;
    }
    // Admin full access
    match /{document=**} {
      allow read, write: if isAdmin();
    }
    // Public reads (published only)
    match /portfolio/{doc} {
      allow read: if resource.data.isPublished == true;
    }
    match /services/{doc} {
      allow read: if resource.data.isPublished == true;
    }
    match /testimonials/{doc} {
      allow read: if resource.data.isPublished == true;
    }
    match /processStages/{doc} {
      allow read: if resource.data.isPublished == true;
    }
    // Always public
    match /siteSettings/{doc} { allow read: if true; }
    match /homepage/{doc} { allow read: if true; }
    match /about/{doc} { allow read: if true; }
    // Leads: admin only
    match /leads/{doc} {
      allow read: if isAdmin();
      allow write: if false;
    }
    // Default deny
    match /{document=**} {
      allow read, write: if false;
    }
  }
}
""")

    # -------------------------------------------------------------
    # SCRIPTS
    # -------------------------------------------------------------
    create_file("scripts/grant-admin.js", """#!/usr/bin/env node
const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  require('dotenv').config({ path: envPath });
}

if (!process.env.FIREBASE_PROJECT_ID || !process.env.FIREBASE_PRIVATE_KEY || !process.env.FIREBASE_CLIENT_EMAIL) {
  console.error('❌ Missing Firebase Admin environment variables.');
  process.exit(1);
}

const args = process.argv.slice(2);
const emailArg = args.find(arg => arg.startsWith('email='));
const email = emailArg ? emailArg.split('=')[1] : null;
if (!email) {
  console.error('❌ Usage: npm run grant-admin -- email=jennifer@example.com');
  process.exit(1);
}

admin.initializeApp({
  credential: admin.credential.cert({
    projectId: process.env.FIREBASE_PROJECT_ID,
    privateKey: process.env.FIREBASE_PRIVATE_KEY.replace(/\\\\n/g, '\\n'),
    clientEmail: process.env.FIREBASE_CLIENT_EMAIL,
  }),
});

async function main() {
  try {
    const user = await admin.auth().getUserByEmail(email);
    console.log(`✅ Found user: ${user.uid} (${user.email})`);
    await admin.auth().setCustomUserClaims(user.uid, { admin: true });
    console.log(`✅ Admin claim granted to ${email}`);
    console.log('📌 User must sign out and back in.');
  } catch (err) {
    console.error('❌ Error:', err.message);
    process.exit(1);
  }
}
main();
""")

    # -------------------------------------------------------------
    # ROOT LAYOUT
    # -------------------------------------------------------------
    create_file("src/app/layout.js", """export const metadata = {
  title: 'Jennifer Ibhafidon | Ghostwriter',
  description: 'Professional ghostwriting services for fiction, non-fiction, and thought leadership.',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en" style={{ margin: 0, padding: 0, background: '#1A4D24' }}>
      <body style={{ margin: 0, padding: 0, background: '#1A4D24', minHeight: '100vh' }}>
        {children}
      </body>
    </html>
  );
}
""")

    # -------------------------------------------------------------
    # FIREBASE CLIENT & ADMIN
    # -------------------------------------------------------------
    create_file("src/lib/firebase/client.js", """import { initializeApp, getApps, getApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';

const firebaseConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
};

const app = getApps().length ? getApp() : initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

export { app, auth, db };
""")

    create_file("src/lib/firebase/admin.js", """import { initializeApp, cert } from 'firebase-admin/app';
import { getAuth } from 'firebase-admin/auth';
import { getFirestore } from 'firebase-admin/firestore';

if (!global._firebaseAdminApp) {
  const privateKey = process.env.FIREBASE_PRIVATE_KEY?.replace(/\\\\n/g, '\\n');
  global._firebaseAdminApp = initializeApp({
    credential: cert({
      projectId: process.env.FIREBASE_PROJECT_ID,
      privateKey,
      clientEmail: process.env.FIREBASE_CLIENT_EMAIL,
    }),
  });
}

const auth = getAuth();
const db = getFirestore();

export { auth, db };
""")

    # -------------------------------------------------------------
    # UTILITY FUNCTIONS
    # -------------------------------------------------------------
    create_file("src/lib/utils/slugify.js", """export function slugify(text) {
  return text
    .toString()
    .toLowerCase()
    .trim()
    .replace(/\\s+/g, '-')
    .replace(/[^\\w\\-]+/g, '')
    .replace(/\\-\\-+/g, '-')
    .replace(/^-+/, '')
    .replace(/-+$/, '');
}
""")

    create_file("src/lib/utils/sanitize.js", """import DOMPurify from 'dompurify';
import { JSDOM } from 'jsdom';

const window = new JSDOM('').window;
const purify = DOMPurify(window);

const ALLOWED_TAGS = ['p','br','strong','em','u','h1','h2','h3','ul','ol','li','blockquote','a'];
const ALLOWED_ATTR = ['href','target'];

export function sanitizeHtml(html) {
  if (!html) return '';
  return purify.sanitize(html, {
    ALLOWED_TAGS,
    ALLOWED_ATTR,
    FORBID_TAGS: ['script','style','iframe','object','embed'],
  });
}
""")

    # -------------------------------------------------------------
    # PUBLIC LAYOUT
    # -------------------------------------------------------------
    create_file("src/app/(public)/layout.js", """'use client';

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
""")

    # -------------------------------------------------------------
    # PUBLIC PAGES (Home, About, Services, Portfolio, Process, Contact)
    # -------------------------------------------------------------
    create_file("src/app/(public)/page.js", """import { db } from '@/lib/firebase/admin';

export const revalidate = 3600;

async function getHomepageData() {
  const homepageDoc = await db.collection('homepage').doc('singleton').get();
  const featuredProjects = await db.collection('portfolio')
    .where('isPublished', '==', true)
    .where('isFeatured', '==', true)
    .get();
  return {
    homepage: homepageDoc.exists ? homepageDoc.data() : null,
    featuredProjects: featuredProjects.docs.map(doc => ({ id: doc.id, ...doc.data() })),
  };
}

export default async function HomePage() {
  const { homepage, featuredProjects } = await getHomepageData();

  const styles = {
    hero: { background: 'linear-gradient(135deg, #0D2E17, #1A4D24, #2D7D3A)', padding: '80px 20px', textAlign: 'center', borderBottom: '3px solid #C9A832' },
    heroTitle: { fontSize: '3rem', fontWeight: 'bold', marginBottom: '1rem', color: '#C9A832', textShadow: '0 2px 4px rgba(0,0,0,0.3)' },
    heroSub: { fontSize: '1.25rem', marginBottom: '2rem', color: '#E8E8E8', opacity: 0.95 },
    goldBtn: { display: 'inline-block', padding: '14px 40px', background: '#C9A832', color: '#0D2E17', borderRadius: '50px', fontWeight: 'bold', textDecoration: 'none', fontSize: '1rem' },
    section: { padding: '60px 20px', maxWidth: '1200px', margin: '0 auto' },
    sectionTitle: { fontSize: '2rem', textAlign: 'center', color: '#C9A832', marginBottom: '40px' },
    grid: { display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '24px' },
    card: { background: '#2D7D3A', borderRadius: '12px', overflow: 'hidden', boxShadow: '0 4px 20px rgba(0,0,0,0.3)', border: '1px solid #3A8F48' },
    cardImg: { width: '100%', height: '200px', objectFit: 'cover', borderBottom: '2px solid #C9A832' },
    cardContent: { padding: '20px' },
    cardTitle: { fontSize: '1.25rem', color: '#C9A832', marginBottom: '8px' },
    cardCat: { color: '#B8D9B8', margin: 0 },
    ctaSection: { padding: '60px 20px', background: '#1A4D24', textAlign: 'center', borderTop: '3px solid #C9A832', borderBottom: '3px solid #C9A832' },
    ctaTitle: { fontSize: '2rem', color: '#C9A832', marginBottom: '16px' },
    ctaBtn: { display: 'inline-block', padding: '14px 40px', background: '#C9A832', color: '#0D2E17', borderRadius: '50px', fontWeight: 'bold', textDecoration: 'none', fontSize: '1rem' },
    empty: { textAlign: 'center', color: '#B8D9B8', fontSize: '1.1rem', padding: '20px' },
  };

  return (
    <>
      <section style={styles.hero}>
        <div style={{ maxWidth: '800px', margin: '0 auto' }}>
          <h1 style={styles.heroTitle}>{homepage?.heroTitle || 'Your Ideas, Crafted into Writing'}</h1>
          <p style={styles.heroSub}>{homepage?.heroSubtext || 'Partner with me to bring your story to life.'}</p>
          <a href="/contact" style={styles.goldBtn}>{homepage?.heroCtaText || 'Work With Me'}</a>
        </div>
      </section>

      <section style={styles.section}>
        <h2 style={styles.sectionTitle}>Featured Work</h2>
        {featuredProjects.length > 0 ? (
          <div style={styles.grid}>
            {featuredProjects.map(p => (
              <div key={p.id} style={styles.card}>
                {p.coverImageUrl && <img src={p.coverImageUrl} alt={p.title} style={styles.cardImg} />}
                <div style={styles.cardContent}>
                  <h3 style={styles.cardTitle}>{p.title}</h3>
                  <p style={styles.cardCat}>{p.category}</p>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <p style={styles.empty}>✨ Portfolio projects will appear here once Jennifer adds them from the admin panel.</p>
        )}
      </section>

      <section style={styles.ctaSection}>
        <div style={{ maxWidth: '600px', margin: '0 auto' }}>
          <h2 style={styles.ctaTitle}>Ready to work together?</h2>
          <a href="/contact" style={styles.ctaBtn}>Let's Talk</a>
        </div>
      </section>
    </>
  );
}
""")

    create_file("src/app/(public)/about/page.js", """import { db } from '@/lib/firebase/admin';

export const revalidate = 3600;

async function getAboutData() {
  const doc = await db.collection('about').doc('singleton').get();
  return doc.exists ? doc.data() : null;
}

export default async function AboutPage() {
  const about = await getAboutData();

  const styles = {
    container: { maxWidth: '900px', margin: '0 auto', padding: '40px 20px' },
    title: { fontSize: '2.5rem', color: '#C9A832', marginBottom: '20px' },
    image: { width: '100%', maxWidth: '300px', borderRadius: '12px', marginBottom: '30px', border: '3px solid #C9A832' },
    bio: { fontSize: '1.1rem', lineHeight: '1.8', marginBottom: '30px', color: '#E8E8E8' },
    philosophy: { fontSize: '1.1rem', lineHeight: '1.8', marginBottom: '30px', background: '#2D7D3A', padding: '30px', borderRadius: '12px', border: '1px solid #3A8F48', color: '#E8E8E8' },
    philosophyTitle: { color: '#C9A832', marginBottom: '10px' },
    specialties: { background: '#0D2E17', padding: '20px 30px', borderRadius: '12px', border: '1px solid #C9A832' },
    specialtiesTitle: { fontSize: '1.2rem', fontWeight: 'bold', color: '#C9A832', marginBottom: '10px' },
    tag: { display: 'inline-block', background: '#2D7D3A', color: '#C9A832', padding: '6px 16px', borderRadius: '20px', margin: '4px 6px 4px 0', fontSize: '0.9rem', border: '1px solid #C9A832' },
    empty: { textAlign: 'center', padding: '60px 20px', color: '#B8D9B8' },
  };

  if (!about) {
    return (
      <div style={styles.empty}>
        <h2 style={{ color: '#C9A832' }}>About Jennifer</h2>
        <p>Professional biography coming soon.</p>
      </div>
    );
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>About Jennifer</h1>
      {about.profileImageUrl && <img src={about.profileImageUrl} alt="Jennifer Ibhafidon" style={styles.image} />}
      {about.biography && <div style={styles.bio} dangerouslySetInnerHTML={{ __html: about.biography }} />}
      {about.philosophy && (
        <div style={styles.philosophy}>
          <h3 style={styles.philosophyTitle}>Writing Philosophy</h3>
          <div dangerouslySetInnerHTML={{ __html: about.philosophy }} />
        </div>
      )}
      {about.specialties && about.specialties.length > 0 && (
        <div style={styles.specialties}>
          <h3 style={styles.specialtiesTitle}>Specialties</h3>
          {about.specialties.map((s, i) => <span key={i} style={styles.tag}>{s}</span>)}
        </div>
      )}
    </div>
  );
}
""")

    create_file("src/app/(public)/services/page.js", """import { db } from '@/lib/firebase/admin';

export const revalidate = 3600;

async function getServices() {
  const snapshot = await db.collection('services')
    .where('isPublished', '==', true)
    .orderBy('order')
    .get();
  return snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
}

export default async function ServicesPage() {
  const services = await getServices();

  const styles = {
    container: { maxWidth: '1000px', margin: '0 auto', padding: '40px 20px' },
    title: { fontSize: '2.5rem', color: '#C9A832', textAlign: 'center', marginBottom: '40px' },
    grid: { display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '24px' },
    card: { background: '#2D7D3A', padding: '30px', borderRadius: '12px', boxShadow: '0 4px 20px rgba(0,0,0,0.3)', border: '1px solid #3A8F48' },
    cardTitle: { fontSize: '1.3rem', color: '#C9A832', marginBottom: '10px' },
    cardDesc: { fontSize: '1rem', lineHeight: '1.6', color: '#B8D9B8' },
    cardCta: { display: 'inline-block', marginTop: '16px', color: '#C9A832', fontWeight: 'bold', textDecoration: 'none' },
    empty: { textAlign: 'center', padding: '60px 20px', color: '#B8D9B8' },
  };

  if (services.length === 0) {
    return (
      <div style={styles.empty}>
        <h2 style={{ color: '#C9A832' }}>Services</h2>
        <p>Service details coming soon.</p>
      </div>
    );
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Services</h1>
      <div style={styles.grid}>
        {services.map(service => (
          <div key={service.id} style={styles.card}>
            <h3 style={styles.cardTitle}>{service.title}</h3>
            <div style={styles.cardDesc} dangerouslySetInnerHTML={{ __html: service.description }} />
            <a href={service.ctaLink || '/contact'} style={styles.cardCta}>{service.ctaText || 'Learn More'} →</a>
          </div>
        ))}
      </div>
    </div>
  );
}
""")

    create_file("src/app/(public)/portfolio/page.js", """import { db } from '@/lib/firebase/admin';
import Link from 'next/link';

export const revalidate = 3600;

async function getPortfolio() {
  const snapshot = await db.collection('portfolio')
    .where('isPublished', '==', true)
    .orderBy('order')
    .get();
  return snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
}

export default async function PortfolioPage() {
  const projects = await getPortfolio();

  const styles = {
    container: { maxWidth: '1200px', margin: '0 auto', padding: '40px 20px' },
    title: { fontSize: '2.5rem', color: '#C9A832', textAlign: 'center', marginBottom: '40px' },
    grid: { display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '24px' },
    card: { background: '#2D7D3A', borderRadius: '12px', overflow: 'hidden', border: '1px solid #3A8F48', transition: 'transform 0.2s', cursor: 'pointer', textDecoration: 'none', color: 'inherit' },
    cardImg: { width: '100%', height: '200px', objectFit: 'cover', borderBottom: '2px solid #C9A832' },
    cardContent: { padding: '20px' },
    cardTitle: { fontSize: '1.25rem', color: '#C9A832', marginBottom: '8px' },
    cardCat: { color: '#B8D9B8', margin: 0 },
    empty: { textAlign: 'center', padding: '60px 20px', color: '#B8D9B8' },
  };

  if (projects.length === 0) {
    return (
      <div style={styles.empty}>
        <h2 style={{ color: '#C9A832' }}>Portfolio</h2>
        <p>Projects coming soon.</p>
      </div>
    );
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Portfolio</h1>
      <div style={styles.grid}>
        {projects.map(p => (
          <Link href={`/portfolio/${p.slug}`} key={p.id} style={styles.card}>
            {p.coverImageUrl && <img src={p.coverImageUrl} alt={p.title} style={styles.cardImg} />}
            <div style={styles.cardContent}>
              <h3 style={styles.cardTitle}>{p.title}</h3>
              <p style={styles.cardCat}>{p.category}</p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
""")

    create_file("src/app/(public)/portfolio/[slug]/page.js", """import { db } from '@/lib/firebase/admin';
import { notFound } from 'next/navigation';

export const revalidate = 3600;

export async function generateStaticParams() {
  const snapshot = await db.collection('portfolio')
    .where('isPublished', '==', true)
    .get();
  return snapshot.docs.map(doc => ({ slug: doc.data().slug }));
}

async function getProject(slug) {
  const snapshot = await db.collection('portfolio')
    .where('slug', '==', slug)
    .where('isPublished', '==', true)
    .limit(1)
    .get();
  if (snapshot.empty) return null;
  const doc = snapshot.docs[0];
  const data = doc.data();
  let testimonial = null;
  if (data.testimonialId) {
    const tDoc = await db.collection('testimonials').doc(data.testimonialId).get();
    if (tDoc.exists && tDoc.data().isPublished) {
      testimonial = { id: tDoc.id, ...tDoc.data() };
    }
  }
  return { id: doc.id, ...data, testimonial };
}

export async function generateMetadata({ params }) {
  const project = await getProject(params.slug);
  if (!project) return { title: 'Not Found' };
  return {
    title: project.metaTitle || `${project.title} | Jennifer Ibhafidon`,
    description: project.metaDescription || project.excerpt || project.description?.slice(0, 160),
    openGraph: {
      title: project.metaTitle || project.title,
      description: project.metaDescription || project.excerpt,
      images: project.coverImageUrl ? [{ url: project.coverImageUrl }] : [],
    },
  };
}

export default async function PortfolioDetailPage({ params }) {
  const project = await getProject(params.slug);
  if (!project) notFound();

  const showClient = project.visibility === 'public' && project.clientName;

  const styles = {
    container: { maxWidth: '900px', margin: '0 auto', padding: '40px 20px' },
    image: { width: '100%', maxHeight: '400px', objectFit: 'cover', borderRadius: '12px', marginBottom: '20px', border: '2px solid #C9A832' },
    title: { fontSize: '2.5rem', color: '#C9A832', marginBottom: '10px' },
    meta: { color: '#B8D9B8', marginBottom: '20px' },
    body: { fontSize: '1.1rem', lineHeight: '1.8', color: '#E8E8E8' },
    gallery: { display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))', gap: '16px', marginTop: '30px' },
    galleryImg: { width: '100%', height: '150px', objectFit: 'cover', borderRadius: '8px', border: '1px solid #3A8F48' },
    testimonial: { background: '#0D2E17', padding: '20px', borderRadius: '12px', marginTop: '30px', border: '1px solid #C9A832' },
    testimonialQuote: { fontSize: '1.2rem', color: '#E8E8E8', fontStyle: 'italic' },
    testimonialCite: { color: '#C9A832', marginTop: '10px', display: 'block' },
  };

  return (
    <div style={styles.container}>
      {project.coverImageUrl && <img src={project.coverImageUrl} alt={project.title} style={styles.image} />}
      <h1 style={styles.title}>{project.title}</h1>
      <div style={styles.meta}>
        {project.category && <span>Category: {project.category}</span>}
        {project.year && <span style={{ marginLeft: '16px' }}>Year: {project.year}</span>}
        {project.jenniferRole && <span style={{ marginLeft: '16px' }}>Role: {project.jenniferRole}</span>}
        {showClient && <span style={{ marginLeft: '16px' }}>Client: {project.clientName}</span>}
      </div>
      <div style={styles.body} dangerouslySetInnerHTML={{ __html: project.description }} />
      {project.galleryImages?.length > 0 && (
        <div style={styles.gallery}>
          {project.galleryImages.map((url, i) => <img key={i} src={url} alt={`${project.title} ${i+1}`} style={styles.galleryImg} />)}
        </div>
      )}
      {project.testimonial && (
        <div style={styles.testimonial}>
          <p style={styles.testimonialQuote}>"{project.testimonial.quote}"</p>
          <cite style={styles.testimonialCite}>
            {project.testimonial.clientName}
            {project.testimonial.clientRole && `, ${project.testimonial.clientRole}`}
          </cite>
        </div>
      )}
    </div>
  );
}
""")

    create_file("src/app/(public)/process/page.js", """import { db } from '@/lib/firebase/admin';

export const revalidate = 3600;

async function getProcessStages() {
  const snapshot = await db.collection('processStages')
    .where('isPublished', '==', true)
    .orderBy('order')
    .get();
  return snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
}

export default async function ProcessPage() {
  const stages = await getProcessStages();

  const styles = {
    container: { maxWidth: '800px', margin: '0 auto', padding: '40px 20px' },
    title: { fontSize: '2.5rem', color: '#C9A832', textAlign: 'center', marginBottom: '40px' },
    step: { display: 'flex', alignItems: 'flex-start', gap: '20px', marginBottom: '30px', background: '#2D7D3A', padding: '20px', borderRadius: '12px', border: '1px solid #3A8F48' },
    number: { fontSize: '2rem', fontWeight: 'bold', color: '#C9A832', minWidth: '50px' },
    content: { flex: 1 },
    stepTitle: { fontSize: '1.3rem', color: '#C9A832', marginBottom: '6px' },
    stepDesc: { color: '#E8E8E8', lineHeight: '1.6' },
    empty: { textAlign: 'center', padding: '60px 20px', color: '#B8D9B8' },
  };

  if (stages.length === 0) {
    return (
      <div style={styles.empty}>
        <h2 style={{ color: '#C9A832' }}>My Writing Process</h2>
        <p>Process details coming soon.</p>
      </div>
    );
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>My Writing Process</h1>
      {stages.map((stage, index) => (
        <div key={stage.id} style={styles.step}>
          <div style={styles.number}>{index + 1}</div>
          <div style={styles.content}>
            <h3 style={styles.stepTitle}>{stage.title}</h3>
            <div style={styles.stepDesc} dangerouslySetInnerHTML={{ __html: stage.description }} />
          </div>
        </div>
      ))}
    </div>
  );
}
""")

    create_file("src/app/(public)/contact/page.js", """'use client';

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
""")

    # -------------------------------------------------------------
    # ADMIN: LOGIN, LAYOUT, DASHBOARD, HOMEPAGE, ABOUT, SERVICES, PORTFOLIO, TESTIMONIALS, PROCESS, LEADS, SETTINGS
    # -------------------------------------------------------------
    create_file("src/app/admin/page.js", """'use client';

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
""")

    create_file("src/app/admin/layout.js", """'use client';

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
""")

    create_file("src/app/admin/dashboard/page.js", """'use client';

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
""")

    create_file("src/app/admin/homepage/page.js", """'use client';

import { useState, useEffect } from 'react';
import { db } from '@/lib/firebase/client';
import { doc, getDoc, setDoc, collection, getDocs, query, where } from 'firebase/firestore';

export default function AdminHomepagePage() {
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);
  const [projects, setProjects] = useState([]);
  const [form, setForm] = useState({
    heroTitle: '',
    heroSubtext: '',
    heroCtaText: '',
    heroCtaLink: '/contact',
    heroImageUrl: '',
    heroImageAlt: '',
    trustBarText: '',
    featuredProjectIds: [],
  });

  useEffect(() => {
    const loadData = async () => {
      try {
        const docRef = doc(db, 'homepage', 'singleton');
        const docSnap = await getDoc(docRef);
        if (docSnap.exists()) setForm(docSnap.data());
        const q = query(collection(db, 'portfolio'), where('isPublished', '==', true));
        const snap = await getDocs(q);
        setProjects(snap.docs.map(d => ({ id: d.id, title: d.data().title })));
      } catch (err) {
        setError('Failed to load: ' + err.message);
      } finally {
        setLoading(false);
      }
    };
    loadData();
  }, []);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    if (type === 'checkbox') {
      setForm(prev => {
        const ids = prev.featuredProjectIds || [];
        if (checked) return { ...prev, featuredProjectIds: [...ids, value] };
        else return { ...prev, featuredProjectIds: ids.filter(id => id !== value) };
      });
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
      const docRef = doc(db, 'homepage', 'singleton');
      await setDoc(docRef, form, { merge: true });
      setSuccess(true);
      await fetch('/api/revalidate', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ path: '/' }) }).catch(() => {});
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
    textarea: { width: '100%', padding: '10px', borderRadius: '8px', border: '1px solid #2D7D3A', background: '#0D2E17', color: '#E8E8E8', fontSize: '1rem', minHeight: '80px' },
    checkboxGroup: { display: 'flex', flexDirection: 'column', gap: '6px', background: '#0D2E17', padding: '12px', borderRadius: '8px', border: '1px solid #2D7D3A' },
    checkboxLabel: { color: '#E8E8E8', display: 'flex', alignItems: 'center', gap: '8px' },
    button: { padding: '12px 24px', background: '#C9A832', color: '#0D2E17', border: 'none', borderRadius: '8px', fontWeight: '700', fontSize: '1rem', cursor: 'pointer' },
    buttonDisabled: { opacity: 0.6, cursor: 'not-allowed' },
    success: { background: '#2D7D3A', padding: '12px', borderRadius: '8px', color: '#C9A832', border: '1px solid #C9A832' },
    error: { background: '#4D1A1A', padding: '12px', borderRadius: '8px', color: '#E8A0A0', border: '1px solid #C9A832' },
  };

  if (loading) return <p style={{ color: '#B8D9B8' }}>Loading...</p>;

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>🏠 Homepage Editor</h1>
      {error && <div style={styles.error}>{error}</div>}
      {success && <div style={styles.success}>✅ Homepage updated!</div>}
      <form onSubmit={handleSubmit} style={styles.form}>
        <div><label style={styles.label}>Hero Title</label><input type="text" name="heroTitle" value={form.heroTitle || ''} onChange={handleChange} style={styles.input} placeholder="Your Ideas, Crafted into Writing" /></div>
        <div><label style={styles.label}>Hero Subtext</label><textarea name="heroSubtext" value={form.heroSubtext || ''} onChange={handleChange} style={styles.textarea} placeholder="Partner with me to bring your story to life." /></div>
        <div><label style={styles.label}>CTA Button Text</label><input type="text" name="heroCtaText" value={form.heroCtaText || ''} onChange={handleChange} style={styles.input} placeholder="Work With Me" /></div>
        <div><label style={styles.label}>CTA Link</label><input type="text" name="heroCtaLink" value={form.heroCtaLink || ''} onChange={handleChange} style={styles.input} placeholder="/contact" /></div>
        <div><label style={styles.label}>Hero Image URL</label><input type="text" name="heroImageUrl" value={form.heroImageUrl || ''} onChange={handleChange} style={styles.input} placeholder="https://example.com/hero.jpg" /></div>
        <div><label style={styles.label}>Trust Bar Text</label><input type="text" name="trustBarText" value={form.trustBarText || ''} onChange={handleChange} style={styles.input} placeholder="Trusted by authors & businesses worldwide" /></div>
        <div>
          <label style={styles.label}>Featured Projects</label>
          <div style={styles.checkboxGroup}>
            {projects.length === 0 ? <p style={{ color: '#B8D9B8' }}>No published projects yet.</p> :
              projects.map(p => (
                <label key={p.id} style={styles.checkboxLabel}>
                  <input type="checkbox" value={p.id} checked={(form.featuredProjectIds || []).includes(p.id)} onChange={handleChange} /> {p.title}
                </label>
              ))
            }
          </div>
        </div>
        <button type="submit" disabled={saving} style={{ ...styles.button, ...(saving ? styles.buttonDisabled : {}) }}>
          {saving ? 'Saving...' : 'Save Homepage'}
        </button>
      </form>
    </div>
  );
}
""")

    create_file("src/app/admin/about/page.js", """'use client';

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
""")

    create_file("src/app/admin/services/page.js", """'use client';

import { useState, useEffect } from 'react';
import { db } from '@/lib/firebase/client';
import { collection, getDocs, addDoc, updateDoc, deleteDoc, doc } from 'firebase/firestore';

export default function AdminServicesPage() {
  const [services, setServices] = useState([]);
  const [loading, setLoading] = useState(true);
  const [editingId, setEditingId] = useState(null);
  const [form, setForm] = useState({ title: '', description: '', ctaText: 'Learn More', ctaLink: '/contact', isPublished: false, order: 0 });
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    loadServices();
  }, []);

  const loadServices = async () => {
    try {
      const snap = await getDocs(collection(db, 'services'));
      const items = snap.docs.map(d => ({ id: d.id, ...d.data() }));
      items.sort((a, b) => a.order - b.order);
      setServices(items);
    } catch (err) {
      setError('Failed to load services.');
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setForm(prev => ({ ...prev, [name]: type === 'checkbox' ? checked : value }));
  };

  const resetForm = () => {
    setForm({ title: '', description: '', ctaText: 'Learn More', ctaLink: '/contact', isPublished: false, order: services.length });
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
      if (editingId) {
        await updateDoc(doc(db, 'services', editingId), form);
      } else {
        await addDoc(collection(db, 'services'), { ...form, order: services.length });
      }
      setSuccess(true);
      await loadServices();
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
    if (!confirm('Delete this service?')) return;
    try {
      await deleteDoc(doc(db, 'services', id));
      await loadServices();
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
      <h1 style={styles.title}>📋 Services</h1>
      {error && <div style={styles.error}>{error}</div>}
      {success && <div style={styles.success}>✅ Service saved!</div>}
      <div style={styles.form}>
        <h3 style={{ color: '#C9A832', marginBottom: '12px' }}>{editingId ? 'Edit Service' : 'Add New Service'}</h3>
        <form onSubmit={handleSubmit}>
          <label style={styles.label}>Title *</label>
          <input type="text" name="title" value={form.title} onChange={handleChange} style={styles.input} required />
          <label style={styles.label}>Description</label>
          <textarea name="description" value={form.description} onChange={handleChange} style={styles.textarea} />
          <label style={styles.label}>CTA Text</label>
          <input type="text" name="ctaText" value={form.ctaText} onChange={handleChange} style={styles.input} />
          <label style={styles.label}>CTA Link</label>
          <input type="text" name="ctaLink" value={form.ctaLinks} onChange={handleChange} style={styles.input} />
          <label style={styles.label}><input type="checkbox" name="isPublished" checked={form.isPublished} onChange={handleChange} style={styles.checkbox} /> Published</label>
          <button type="submit" disabled={submitting} style={styles.button}>{submitting ? 'Saving...' : 'Save'}</button>
          <button type="button" onClick={resetForm} style={{ ...styles.button, background: '#6B8C6B', marginLeft: '12px' }}>Cancel</button>
        </form>
      </div>
      <table style={styles.table}>
        <thead><tr><th style={styles.th}>Title</th><th style={styles.th}>Status</th><th style={styles.th}>Actions</th></tr></thead>
        <tbody>
          {services.map(item => (
            <tr key={item.id}>
              <td style={styles.td}>{item.title}</td>
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
""")

    create_file("src/app/admin/portfolio/page.js", """'use client';

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
""")

    create_file("src/app/admin/testimonials/page.js", """'use client';

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
""")

    create_file("src/app/admin/process/page.js", """'use client';

import { useState, useEffect } from 'react';
import { db } from '@/lib/firebase/client';
import { collection, getDocs, addDoc, updateDoc, deleteDoc, doc } from 'firebase/firestore';

export default function AdminProcessPage() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [editingId, setEditingId] = useState(null);
  const [form, setForm] = useState({ title: '', description: '', iconName: '', isPublished: true, order: 0 });
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => { loadItems(); }, []);

  const loadItems = async () => {
    try {
      const snap = await getDocs(collection(db, 'processStages'));
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
    setForm({ title: '', description: '', iconName: '', isPublished: true, order: items.length });
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
      if (editingId) await updateDoc(doc(db, 'processStages', editingId), form);
      else await addDoc(collection(db, 'processStages'), { ...form, order: items.length });
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
  const handleDelete = async (id) => { if (!confirm('Delete?')) return; await deleteDoc(doc(db, 'processStages', id)); await loadItems(); };

  const styles = {
    container: { padding: '20px', maxWidth: '800px', margin: '0 auto' },
    title: { color: '#C9A832', fontSize: '1.8rem', marginBottom: '20px' },
    form: { background: '#0D2E17', padding: '20px', borderRadius: '12px', border: '1px solid #2D7D3A', marginBottom: '30px' },
    label: { color: '#C9A832', fontWeight: '600', display: 'block', marginBottom: '4px' },
    input: { width: '100%', padding: '10px', borderRadius: '8px', border: '1px solid #2D7D3A', background: '#1A4D24', color: '#E8E8E8', fontSize: '1rem', marginBottom: '12px' },
    textarea: { width: '100%', padding: '10px', borderRadius: '8px', border: '1px solid #2D7D3A', background: '#1A4D24', color: '#E8E8E8', fontSize: '1rem', minHeight: '60px', marginBottom: '12px' },
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
      <h1 style={styles.title}>🔄 Process Stages</h1>
      {error && <div style={styles.error}>{error}</div>}
      {success && <div style={styles.success}>✅ Saved!</div>}
      <div style={styles.form}>
        <h3 style={{ color: '#C9A832', marginBottom: '12px' }}>{editingId ? 'Edit' : 'Add'} Stage</h3>
        <form onSubmit={handleSubmit}>
          <label style={styles.label}>Title *</label>
          <input type="text" name="title" value={form.title} onChange={handleChange} style={styles.input} required />
          <label style={styles.label}>Description</label>
          <textarea name="description" value={form.description} onChange={handleChange} style={styles.textarea} />
          <label style={styles.label}>Icon Name (optional)</label>
          <input type="text" name="iconName" value={form.iconName} onChange={handleChange} style={styles.input} />
          <label style={styles.label}><input type="checkbox" name="isPublished" checked={form.isPublished} onChange={handleChange} style={styles.checkbox} /> Published</label>
          <button type="submit" disabled={submitting} style={styles.button}>{submitting ? 'Saving...' : 'Save'}</button>
          <button type="button" onClick={resetForm} style={{ ...styles.button, background: '#6B8C6B', marginLeft: '12px' }}>Cancel</button>
        </form>
      </div>
      <table style={styles.table}>
        <thead><tr><th style={styles.th}>Title</th><th style={styles.th}>Status</th><th style={styles.th}>Actions</th></tr></thead>
        <tbody>
          {items.map(item => (
            <tr key={item.id}>
              <td style={styles.td}>{item.title}</td>
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
""")

    create_file("src/app/admin/leads/page.js", """'use client';

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
""")

    create_file("src/app/admin/settings/page.js", """'use client';

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
""")

    # -------------------------------------------------------------
    # API ROUTES
    # -------------------------------------------------------------
    create_file("src/app/api/leads/route.js", """import { db } from '@/lib/firebase/admin';

const rateLimit = new Map();

function getClientIP(request) {
  const forwarded = request.headers.get('x-forwarded-for');
  return forwarded ? forwarded.split(',')[0] : 'unknown';
}

function isRateLimited(ip) {
  const now = Date.now();
  const window = 3600000;
  const maxRequests = 5;
  if (!rateLimit.has(ip)) rateLimit.set(ip, []);
  const timestamps = rateLimit.get(ip).filter(t => now - t < window);
  timestamps.push(now);
  rateLimit.set(ip, timestamps);
  return timestamps.length > maxRequests;
}

export async function POST(request) {
  const ip = getClientIP(request);
  if (isRateLimited(ip)) {
    return new Response(JSON.stringify({ error: 'Too many requests' }), { status: 429, headers: { 'Content-Type': 'application/json' } });
  }
  let body;
  try { body = await request.json(); } catch { return new Response(JSON.stringify({ error: 'Invalid JSON' }), { status: 400, headers: { 'Content-Type': 'application/json' } }); }
  const { name, email, projectType, description, timeline } = body;
  if (!name || name.length > 100) return new Response(JSON.stringify({ error: 'Name required (max 100 chars)' }), { status: 400, headers: { 'Content-Type': 'application/json' } });
  if (!email || !/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email)) return new Response(JSON.stringify({ error: 'Valid email required' }), { status: 400, headers: { 'Content-Type': 'application/json' } });
  if (!description || description.length > 5000) return new Response(JSON.stringify({ error: 'Description required (max 5000 chars)' }), { status: 400, headers: { 'Content-Type': 'application/json' } });
  try {
    await db.collection('leads').add({ name: name.trim(), email: email.trim(), projectType: projectType || null, description: description.trim(), timeline: timeline || null, status: 'new', createdAt: new Date().toISOString() });
    return new Response(JSON.stringify({ success: true }), { status: 200, headers: { 'Content-Type': 'application/json' } });
  } catch (err) {
    console.error('Lead error:', err);
    return new Response(JSON.stringify({ error: 'Internal server error' }), { status: 500, headers: { 'Content-Type': 'application/json' } });
  }
}
""")

    create_file("src/app/api/test/route.js", """import { db } from '@/lib/firebase/admin';

export async function GET() {
  try {
    const doc = await db.collection('siteSettings').doc('singleton').get();
    const data = doc.exists ? doc.data() : null;
    return new Response(JSON.stringify({ success: true, data }), { status: 200, headers: { 'Content-Type': 'application/json' } });
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), { status: 500, headers: { 'Content-Type': 'application/json' } });
  }
}
""")

    create_file("src/app/api/revalidate/route.js", """import { revalidatePath } from 'next/cache';

export async function POST(request) {
  const authHeader = request.headers.get('Authorization');
  const token = authHeader?.split('Bearer ')[1];
  if (token !== process.env.REVALIDATE_SECRET) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401, headers: { 'Content-Type': 'application/json' } });
  }
  try {
    const { path } = await request.json();
    if (!path) return new Response(JSON.stringify({ error: 'Missing path' }), { status: 400 });
    revalidatePath(path);
    return new Response(JSON.stringify({ success: true, revalidated: path }), { status: 200, headers: { 'Content-Type': 'application/json' } });
  } catch (error) {
    console.error('Revalidate error:', error);
    return new Response(JSON.stringify({ error: 'Revalidation failed' }), { status: 500, headers: { 'Content-Type': 'application/json' } });
  }
}
""")

    create_file("src/app/api/upload/route.js", """import { auth } from '@/lib/firebase/admin';
import { getStore } from '@netlify/blobs';
import { randomUUID } from 'crypto';

const ALLOWED_TYPES = ['image/jpeg', 'image/png', 'image/webp'];
const MAX_SIZE = 5 * 1024 * 1024;

export async function POST(request) {
  const authHeader = request.headers.get('Authorization');
  const token = authHeader?.split('Bearer ')[1];
  if (!token) return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  let decodedToken;
  try { decodedToken = await auth.verifyIdToken(token); if (!decodedToken.admin) return new Response(JSON.stringify({ error: 'Forbidden' }), { status: 403 }); } catch { return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 }); }
  const formData = await request.formData();
  const file = formData.get('file');
  const path = formData.get('path');
  if (!file || !path) return new Response(JSON.stringify({ error: 'Missing file or path' }), { status: 400 });
  if (!ALLOWED_TYPES.includes(file.type)) return new Response(JSON.stringify({ error: 'Invalid file type. Allowed: JPEG, PNG, WebP' }), { status: 400 });
  if (file.size > MAX_SIZE) return new Response(JSON.stringify({ error: 'File too large. Max: 5MB' }), { status: 400 });
  const store = getStore('media');
  const key = `${path}/${randomUUID()}.${file.name.split('.').pop()}`;
  try {
    await store.set(key, Buffer.from(await file.arrayBuffer()));
    return new Response(JSON.stringify({ success: true, key }), { status: 200, headers: { 'Content-Type': 'application/json' } });
  } catch (error) {
    console.error('Upload error:', error);
    return new Response(JSON.stringify({ error: 'Upload failed' }), { status: 500 });
  }
}
""")

    create_file("src/app/api/delete-blob/route.js", """import { auth } from '@/lib/firebase/admin';
import { getStore } from '@netlify/blobs';

export async function POST(request) {
  const authHeader = request.headers.get('Authorization');
  const token = authHeader?.split('Bearer ')[1];
  if (!token) return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  let decodedToken;
  try { decodedToken = await auth.verifyIdToken(token); if (!decodedToken.admin) return new Response(JSON.stringify({ error: 'Forbidden' }), { status: 403 }); } catch { return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 }); }
  const { key } = await request.json();
  if (!key) return new Response(JSON.stringify({ error: 'Missing key' }), { status: 400 });
  try {
    const store = getStore('media');
    await store.delete(key);
    return new Response(JSON.stringify({ success: true }), { status: 200, headers: { 'Content-Type': 'application/json' } });
  } catch (error) {
    console.error('Delete error:', error);
    return new Response(JSON.stringify({ error: 'Delete failed' }), { status: 500 });
  }
}
""")

    create_file("src/app/api/image/[...key]/route.js", """import { getStore } from '@netlify/blobs';

export async function GET(request, { params }) {
  const { key } = params;
  const store = getStore('media');
  try {
    const blob = await store.get(key.join('/'));
    if (!blob) return new Response('Not found', { status: 404 });
    const ext = key.join('/').split('.').pop().toLowerCase();
    const contentTypeMap = { jpg: 'image/jpeg', jpeg: 'image/jpeg', png: 'image/png', webp: 'image/webp' };
    const contentType = contentTypeMap[ext] || 'application/octet-stream';
    return new Response(blob, { headers: { 'Content-Type': contentType, 'Cache-Control': 'public, max-age=31536000, immutable' } });
  } catch (error) {
    console.error('Image serve error:', error);
    return new Response('Internal server error', { status: 500 });
  }
}
""")

    create_file("src/app/api/portfolio/[id]/route.js", """import { auth, db } from '@/lib/firebase/admin';
import { getStore } from '@netlify/blobs';

export async function DELETE(request, { params }) {
  const { id } = params;
  const authHeader = request.headers.get('Authorization');
  const token = authHeader?.split('Bearer ')[1];
  if (!token) return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  let decodedToken;
  try { decodedToken = await auth.verifyIdToken(token); if (!decodedToken.admin) return new Response(JSON.stringify({ error: 'Forbidden' }), { status: 403 }); } catch { return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 }); }
  const doc = await db.collection('portfolio').doc(id).get();
  if (!doc.exists) return new Response(JSON.stringify({ error: 'Not found' }), { status: 404 });
  const data = doc.data();
  const blobKeys = [];
  if (data.coverImageUrl) { const match = data.coverImageUrl.match(/\\/api\\/image\\/(.+)/); if (match) blobKeys.push(match[1]); }
  if (data.galleryImages) {
    for (const url of data.galleryImages) { const match = url.match(/\\/api\\/image\\/(.+)/); if (match) blobKeys.push(match[1]); }
  }
  await db.collection('portfolio').doc(id).delete();
  const store = getStore('media');
  const deleteErrors = [];
  for (const key of blobKeys) {
    try { await store.delete(key); } catch (err) { console.error(`Failed to delete ${key}:`, err); deleteErrors.push(key); }
  }
  return new Response(JSON.stringify({ success: true, deletedBlobs: blobKeys.length - deleteErrors.length, errors: deleteErrors.length > 0 ? deleteErrors : undefined }), { status: 200, headers: { 'Content-Type': 'application/json' } });
}
""")

    # -------------------------------------------------------------
    # FINAL
    # -------------------------------------------------------------
    print("\n✅ ALL FILES CREATED SUCCESSFULLY!")
    print("\n📋 Next steps:")
    print("   1. Run 'npm install'")
    print("   2. Copy .env.example to .env.local and fill in values (already filled with your config)")
    print("   3. Run 'npm run dev' to start the development server")
    print("   4. Visit http://localhost:3000/admin to log in")
    print("\n🔑 Admin credentials:")
    print("   Email: ibhafidonjennifer4@gmail.com")
    print("   Password: (the one you set in Firebase Console)")

if __name__ == '__main__':
    main()