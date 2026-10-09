"""Reapply the shared navigation to Hexo-generated pages without editing articles.

Run with Python 3 from any directory. Handwritten personal pages are left intact.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://ruguo0119.github.io"


def navigation(active="blog"):
    links = [("home", "/", "首页"), ("blog", "/archives/", "博客"), ("about", "/about/", "关于")]
    items = "".join(
        f'<li class="menu-item"><a href="{url}"' + (' aria-current="page"' if key == active else '') + f'>{label}</a></li>'
        for key, url, label in links
    )
    return '<nav class="site-nav" aria-label="主导航"><ul class="site-links">' + items + '</ul></nav>'


def update(source):
    if 'class="personal-site"' in source:
        return source
    patched, count = re.subn(r'<nav class="site-nav"(?: aria-label="主导航")?>[\s\S]*?</nav>', navigation(), source)
    if count != 1:
        raise ValueError(f"Expected one main navigation, got {count}")
    head, tail = patched.split('</head>', 1)
    head = head.replace('http://example.com', ORIGIN).replace('"hostname":"example.com"', '"hostname":"ruguo0119.github.io"')
    if 'href="/css/site.css"' not in head:
        head = head.replace('<link rel="stylesheet" href="/css/main.css">', '<link rel="stylesheet" href="/css/main.css">\n<link rel="stylesheet" href="/css/site.css">')
    tail = re.sub(r'(<link itemprop="mainEntityOfPage" href=")http://example.com', r'\1' + ORIGIN, tail)
    return head + '</head>' + tail


if __name__ == '__main__':
    changed = []
    for path in sorted(ROOT.rglob('*.html')):
        original = path.read_bytes().decode('utf-8')
        result = update(original)
        if result != original:
            path.write_bytes(result.encode('utf-8'))
            changed.append(path.relative_to(ROOT).as_posix())
    print(f"Updated {len(changed)} pages: " + ', '.join(changed))
