#!/usr/bin/env bash
# Build docs/<skill>.zip for the claude.ai upload path (Settings → Capabilities → Skills).
# claude.ai expects the skill folder (containing SKILL.md) at the zip root.
# Usage: scripts/build-skill-zip.sh <skill-name>
set -euo pipefail
if [ $# -ne 1 ]; then
  echo "usage: scripts/build-skill-zip.sh <skill-name>" >&2
  exit 2
fi
skill="$1"
if ! [[ "$skill" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "skill name must be lowercase letters, digits, and hyphens: $skill" >&2
  exit 2
fi
root="$(cd "$(dirname "$0")/.." && pwd)"
[ -f "$root/skills/$skill/SKILL.md" ] || { echo "no skills/$skill/SKILL.md" >&2; exit 1; }
out="$root/docs/$skill.zip"
rm -f "$out"
(cd "$root/skills" && zip -qr -X "$out" "$skill" -x '*/.DS_Store')
echo "wrote $out"; unzip -l "$out"
