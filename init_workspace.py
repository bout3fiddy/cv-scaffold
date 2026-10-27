"""Create private working files without overwriting existing content."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent


def initialize(root=ROOT):
    copies = {
        'profile/ground-truth.md': 'profile/ground-truth.example.md',
        'profile/preferences.md': 'templates/preferences.md',
        'personal/master/resume.html': 'examples/software-engineering.html',
        'personal/master/cover-letter.md': 'examples/cover-letter.md',
        'personal/master/review.md': 'templates/review.md',
    }
    created = []
    for target, source in copies.items():
        output = root / target
        if output.exists():
            continue
        output.parent.mkdir(parents=True, exist_ok=True)
        content = (root / source).read_text(encoding='utf-8')
        if target.endswith('.html'):
            content = re.sub(r'href="\.\./(design/cv/[^"/]+\.css)"', r'href="../../\1"', content)
        with output.open('x', encoding='utf-8') as stream:
            stream.write(content)
        created.append(target)
    status = root / 'personal/status.md'
    if not status.exists():
        status.write_text('# Working status\n\n- Stage: intake; sources still contain fictional content.\n'
                          '- Next action: interview the user and complete the ground-truth ledger.\n'
                          '- Approved master: none.\n', encoding='utf-8')
        created.append('personal/status.md')
    return created


if __name__ == '__main__':
    for name in initialize():
        print('Created', name)
    print('Ready for the fact interview. Existing files were preserved.')
