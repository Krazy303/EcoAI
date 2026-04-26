import os
import re

files = ['index.html', 'classify.html', 'impact.html', 'about.html', 'education.html']
directory = '/home/rushikesh/wastt/ecoai-website/'

overrides = {
    'text-on-background': 'dark:text-zinc-100',
    'text-on-surface': 'dark:text-zinc-100',
    'text-on-surface-variant': 'dark:text-zinc-400',
    'text-slate-600': 'dark:text-zinc-400',
    'text-zinc-600': 'dark:text-zinc-400',
    'text-slate-500': 'dark:text-zinc-500',
    'text-zinc-500': 'dark:text-zinc-500',
    'text-slate-900': 'dark:text-white',
    'text-zinc-900': 'dark:text-white',
    'bg-white': 'dark:bg-zinc-900',
    'bg-surface-container-lowest': 'dark:bg-zinc-900',
    'bg-surface-container-low': 'dark:bg-zinc-900',
    'bg-surface-container': 'dark:bg-zinc-800',
    'bg-surface-container-high': 'dark:bg-zinc-800',
}

class_regex = re.compile(r'class="([^"]*)"')

for filename in files:
    filepath = os.path.join(directory, filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Pre-clean the mess from previous runs
    content = content.replace('text-on-surface dark:text-zinc-100-variant', 'text-on-surface-variant')
    
    def apply_overrides(match):
        classes = match.group(1).split()
        new_classes = []
        for c in classes:
            new_classes.append(c)
            if c in overrides:
                target = overrides[c]
                if target not in classes:
                    new_classes.append(target)
        
        # Deduplicate while preserving order
        seen = set()
        final = []
        for c in new_classes:
            if c not in seen:
                final.append(c)
                seen.add(c)
        return f'class="{" ".join(final)}"'

    content = class_regex.sub(apply_overrides, content)
    
    # Ensure body has dark:text-zinc-100
    if '<body' in content:
        content = re.sub(r'(<body[^>]*class=")([^"]*)(")', 
                         lambda m: f'{m.group(1)}{m.group(2)} dark:text-zinc-100{m.group(3)}' if 'dark:text-zinc-100' not in m.group(2) else m.group(0), 
                         content)

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Processed {filename}")
