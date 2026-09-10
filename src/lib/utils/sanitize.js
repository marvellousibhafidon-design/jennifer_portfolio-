import DOMPurify from 'isomorphic-dompurify';

const ALLOWED_TAGS = ['p','br','strong','em','u','h1','h2','h3','ul','ol','li','blockquote','a'];
const ALLOWED_ATTR = ['href','target'];

export function sanitizeHtml(html) {
  if (!html) return '';
  return DOMPurify.sanitize(html, {
    ALLOWED_TAGS,
    ALLOWED_ATTR,
    FORBID_TAGS: ['script','style','iframe','object','embed'],
  });
}