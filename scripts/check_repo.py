#!/usr/bin/env python3
"""Repository checks. No dependencies, no model calls.

1. Every skills/<name>/SKILL.md has valid frontmatter (Agent Skills spec:
   name matches the folder, lowercase with hyphens, at most 64 characters;
   description present, at most 1024 characters).
2. Every docs/<name>.zip holds exactly the files in skills/<name>/.
3. Every relative link in docs/*.html and the top-level Markdown files
   points at a file that exists.

Usage: python3 scripts/check_repo.py   (exit 0 = clean, 1 = problems)
"""
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = {".DS_Store"}
problems = []


def fail(msg):
    problems.append(msg)


def frontmatter(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fields = {}
    for line in m.group(1).splitlines():
        if re.match(r"[A-Za-z][\w-]*:", line):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip().strip('"')
    return fields


def check_skills():
    skills_dir = os.path.join(ROOT, "skills")
    names = sorted(d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d)))
    for name in names:
        path = os.path.join(skills_dir, name, "SKILL.md")
        if not os.path.isfile(path):
            fail(f"skills/{name}: no SKILL.md")
            continue
        fm = frontmatter(path)
        if fm is None:
            fail(f"skills/{name}/SKILL.md: no YAML frontmatter")
            continue
        if fm.get("name") != name:
            fail(f"skills/{name}/SKILL.md: name '{fm.get('name')}' does not match the folder")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
            fail(f"skills/{name}: name must be lowercase letters, digits, and single hyphens, at most 64 characters")
        desc = fm.get("description", "")
        if not desc:
            fail(f"skills/{name}/SKILL.md: description is empty")
        elif len(desc) > 1024:
            fail(f"skills/{name}/SKILL.md: description is {len(desc)} characters, the limit is 1024")
    return names


def source_files(name):
    base = os.path.join(ROOT, "skills", name)
    out = {}
    for folder, _, files in os.walk(base):
        for f in files:
            if f in SKIP:
                continue
            full = os.path.join(folder, f)
            rel = name + "/" + os.path.relpath(full, base).replace(os.sep, "/")
            out[rel] = open(full, "rb").read()
    return out


def check_zips(names):
    for name in names:
        zpath = os.path.join(ROOT, "docs", name + ".zip")
        if not os.path.isfile(zpath):
            fail(f"docs/{name}.zip is missing. Run scripts/build-skill-zip.sh {name}")
            continue
        src = source_files(name)
        with zipfile.ZipFile(zpath) as z:
            zipped = {i.filename: z.read(i) for i in z.infolist() if not i.is_dir()}
        for rel in sorted(set(src) - set(zipped)):
            fail(f"docs/{name}.zip lacks {rel}")
        for rel in sorted(set(zipped) - set(src)):
            fail(f"docs/{name}.zip holds {rel}, which is not in skills/{name}/")
        for rel in sorted(set(src) & set(zipped)):
            if src[rel] != zipped[rel]:
                fail(f"docs/{name}.zip: {rel} differs from the source. Run scripts/build-skill-zip.sh {name}")


def check_links():
    pages = [os.path.join(ROOT, "docs", f) for f in sorted(os.listdir(os.path.join(ROOT, "docs"))) if f.endswith(".html")]
    for page in pages:
        text = open(page, encoding="utf-8").read()
        for target in re.findall(r'(?:href|src)="([^"]+)"', text):
            check_target(page, target)
    for md in sorted(f for f in os.listdir(ROOT) if f.endswith(".md")):
        text = open(os.path.join(ROOT, md), encoding="utf-8").read()
        for target in re.findall(r"\]\(([^)\s]+)\)", text):
            check_target(os.path.join(ROOT, md), target)


def check_target(source, target):
    if re.match(r"[a-z]+:", target) or target.startswith(("#", "//")):
        return
    path = target.split("#")[0].split("?")[0]
    if not path:
        return
    full = os.path.normpath(os.path.join(os.path.dirname(source), path))
    if not os.path.exists(full):
        fail(f"{os.path.relpath(source, ROOT)}: link to '{target}' does not resolve")


names = check_skills()
check_zips(names)
check_links()
for p in problems:
    print("FAIL", p)
print(f"{len(names)} skills checked, {len(problems)} problems")
sys.exit(1 if problems else 0)
