#!/usr/bin/env python3
"""
Jennifer Ibhafidon Portfolio - Project Structure Generator
"""
import json
from pathlib import Path

PROJECT_ROOT = Path.cwd()

directories = [
    "src/app/(public)",
    "src/app/(public)/about",
    "src/app/(public)/services",
    "src/app/(public)/portfolio",
    "src/app/(public)/portfolio/[slug]",
    "src/app/(public)/process",
    "src/app/(public)/contact",
    "src/app/(admin)/admin",
    "src/app/(admin)/admin/homepage",
    "src/app/(admin)/admin/about",
    "src/app/(admin)/admin/services",
    "src/app/(admin)/admin/portfolio",
    "src/app/(admin)/admin/portfolio/[id]",
    "src/app/(admin)/admin/testimonials",
    "src/app/(admin)/admin/process",
    "src/app/(admin)/admin/leads",
    "src/app/(admin)/admin/settings",
    "src/app/api/leads",
    "src/app/api/revalidate",
    "src/app/api/upload",
    "src/app/api/delete-blob",
    "src/app/api/image/[...key]",
    "src/app/api/portfolio/[id]",
    "src/components/ui",
    "src/components/public",
    "src/components/admin",
    "src/lib/firebase",
    "src/lib/hooks",
    "src/lib/utils",
    "scripts",
    "public",
]

files = {}

files[".env.example"] = """# Public (safe for client)
NEXT_PUBLIC_FIREBASE_API_KEY=
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=
NEXT_PUBLIC_FIREBASE_PROJECT_ID=
NEXT_PUBLIC_FIREBASE_APP_ID=
NEXT_PUBLIC_SITE_URL=

# Server-Only (NEVER use NEXT_PUBLIC_ prefix)
FIREBASE_PROJECT_ID=
FIREBASE_PRIVATE_KEY=
FIREBASE_CLIENT_EMAIL=
REVALIDATE_SECRET=
"""

files[".gitignore"] = """# dependencies
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
"""

files["package.json"] = json.dumps({
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
        "typescript": "latest"
    }
}, indent=2)

files["next.config.js"] = """/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    serverActions: true,
  },
  images: {
    remotePatterns: [],
  },
}
module.exports = nextConfig
"""

files["firestore.rules"] = """rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    function isAdmin() {
      return request.auth != null && request.auth.token.admin == true;
    }
    match /portfolio/{doc} {
      allow read: if resource.data.isPublished == true;
      allow read: if isAdmin();
      allow write: if isAdmin();
    }
    match /services/{doc} {
      allow read: if resource.data.isPublished == true;
      allow read: if isAdmin();
      allow write: if isAdmin();
    }
    match /testimonials/{doc} {
      allow read: if resource.data.isPublished == true;
      allow read: if isAdmin();
      allow write: if isAdmin();
    }
    match /processStages/{doc} {
      allow read: if resource.data.isPublished == true;
      allow read: if isAdmin();
      allow write: if isAdmin();
    }
    match /siteSettings/{doc} { allow read: if true; allow write: if isAdmin(); }
    match /homepage/{doc} { allow read: if true; allow write: if isAdmin(); }
    match /about/{doc} { allow read: if true; allow write: if isAdmin(); }
    match /leads/{doc} {
      allow read: if isAdmin();
      allow write: if false;
    }
    match /{document=**} {
      allow read, write: if false;
    }
  }
}
"""

files["scripts/grant-admin.js"] = """#!/usr/bin/env node
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
    await admin.auth().setCustomUserClaims(user.uid, { admin: true });
    console.log(`✅ Admin claim granted to ${email}`);
    console.log('📌 User must sign out and back in.');
  } catch (err) {
    console.error('❌ Error:', err.message);
    process.exit(1);
  }
}
main();
"""

# ---- Public routes ----
for route in [
    "src/app/(public)/page.js",
    "src/app/(public)/about/page.js",
    "src/app/(public)/services/page.js",
    "src/app/(public)/portfolio/page.js",
    "src/app/(public)/portfolio/[slug]/page.js",
    "src/app/(public)/process/page.js",
    "src/app/(public)/contact/page.js",
]:
    files[route] = f"// {route.split('/')[-1]} – Phase 1\nexport default function Page() {{ return null; }}"

# ---- Admin routes ----
for route in [
    "src/app/(admin)/admin/page.js",
    "src/app/(admin)/admin/homepage/page.js",
    "src/app/(admin)/admin/about/page.js",
    "src/app/(admin)/admin/services/page.js",
    "src/app/(admin)/admin/portfolio/page.js",
    "src/app/(admin)/admin/portfolio/[id]/page.js",
    "src/app/(admin)/admin/testimonials/page.js",
    "src/app/(admin)/admin/process/page.js",
    "src/app/(admin)/admin/leads/page.js",
    "src/app/(admin)/admin/settings/page.js",
]:
    name = route.split('/')[-1].replace('.js','')
    files[route] = f"// {name} – Phase 2\nexport default function Admin{name.capitalize()}Page() {{ return null; }}"

# ---- API routes ----
for path, method in {
    "src/app/api/leads/route.js": "POST /api/leads",
    "src/app/api/revalidate/route.js": "POST /api/revalidate",
    "src/app/api/upload/route.js": "POST /api/upload",
    "src/app/api/delete-blob/route.js": "POST /api/delete-blob",
    "src/app/api/image/[...key]/route.js": "GET /api/image/[...key]",
    "src/app/api/portfolio/[id]/route.js": "DELETE /api/portfolio/[id]",
}.items():
    files[path] = f"// {method} – Phase 1\nexport async function {method.split(' ')[0]}() {{ return new Response(null, {{ status: 501 }}); }}"

# ---- Lib files ----
files["src/lib/firebase/client.js"] = """import { initializeApp, getApps, getApp } from 'firebase/app';
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
"""

files["src/lib/firebase/admin.js"] = """import admin from 'firebase-admin';

if (!admin.apps.length) {
  const privateKey = process.env.FIREBASE_PRIVATE_KEY?.replace(/\\\\n/g, '\\n');
  admin.initializeApp({
    credential: admin.credential.cert({
      projectId: process.env.FIREBASE_PROJECT_ID,
      privateKey,
      clientEmail: process.env.FIREBASE_CLIENT_EMAIL,
    }),
  });
}

const auth = admin.auth();
const db = admin.firestore();

export { auth, db };
"""

files["src/lib/hooks/useAuth.js"] = """import { useEffect, useState } from 'react';
import { auth } from '@/lib/firebase/client';
import { onAuthStateChanged } from 'firebase/auth';

export function useAuth() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      setUser(user);
      setLoading(false);
    });
    return () => unsubscribe();
  }, []);

  return { user, loading };
}
"""

files["src/lib/hooks/useFirestoreQuery.js"] = """import { useEffect, useState } from 'react';
import { collection, query, getDocs } from 'firebase/firestore';
import { db } from '@/lib/firebase/client';

export function useFirestoreQuery(collectionName, constraints = []) {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const q = query(collection(db, collectionName), ...constraints);
        const snapshot = await getDocs(q);
        setData(snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() })));
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [collectionName, JSON.stringify(constraints)]);

  return { data, loading, error };
}
"""

files["src/lib/utils/slugify.js"] = """export function slugify(text) {
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
"""

files["src/lib/utils/sanitize.js"] = """import DOMPurify from 'dompurify';
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
"""

# ---- Component stubs (ALL return null — no JSX errors) ----
for comp in ["Button","Input","Card","Modal"]:
    files[f"src/components/ui/{comp}.js"] = f"export function {comp}() {{ return null; }}"

for comp in ["Hero","PortfolioGrid","ProcessTimeline"]:
    files[f"src/components/public/{comp}.js"] = f"export function {comp}() {{ return null; }}"

for comp in ["DashboardLayout","Forms","SortableList"]:
    files[f"src/components/admin/{comp}.js"] = f"export function {comp}() {{ return null; }}"

# ---- Public static ----
files["public/robots.txt"] = """User-agent: *
Allow: /
Disallow: /admin/
"""
files["public/favicon.ico"] = ""

# ---- Runner ----
def main():
    print(f"📁 Creating project skeleton in: {PROJECT_ROOT}")
    for d in directories:
        (PROJECT_ROOT / d).mkdir(parents=True, exist_ok=True)
        print(f"  📁 {d}/")
    for rel_path, content in files.items():
        path = PROJECT_ROOT / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  📄 {rel_path}")
    print("\n✅ Skeleton created successfully.")
    print("\nNext steps:")
    print("  1. npm install")
    print("  2. copy .env.example .env.local  (then edit with Firebase values)")
    print("  3. firebase deploy --only firestore:rules")
    print("  4. npm run grant-admin -- email=your_admin_email@example.com")
    print("  5. Push to Netlify (auto-detects Next.js)")

if __name__ == "__main__":
    main()