#!/usr/bin/env node
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
    privateKey: process.env.FIREBASE_PRIVATE_KEY.replace(/\\n/g, '\n'),
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
