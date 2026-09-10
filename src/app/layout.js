export const metadata = {
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
