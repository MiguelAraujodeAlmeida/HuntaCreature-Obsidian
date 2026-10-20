"""Validate this vault without Obsidian, network access or third-party packages."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "context-manifest.json"
IGNORED = {".git", ".obsidian", ".trash", "__pycache__"}
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--refresh", action="store_true", help="Update declared file hashes after reviewing changes")
args = parser.parse_args()
manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
errors = []
groups = ["entrypoints", "current", "reference", "assets"]
declared = [name for group in groups for name in manifest[group]]
if len(declared) != len(set(declared)):
    errors.append("Duplicate manifest entries")
if not re.fullmatch(r"CTX-\d{4}-\d{2}-\d{2}-\d{2}", manifest["context_revision"]):
    errors.append("Invalid context revision")
paths = {}
for name in declared:
    p = (ROOT / name).resolve()
    if not p.is_relative_to(ROOT) or not p.is_file():
        errors.append("Missing or unsafe file: " + name)
    else:
        paths[name] = p
notes = {p.relative_to(ROOT).as_posix(): p for p in ROOT.rglob("*.md")
         if not any(part in IGNORED for part in p.relative_to(ROOT).parts)}
expected = {name for name in declared if name.endswith(".md")}
for name in sorted(set(notes) - expected):
    errors.append("Unclassified note: " + name)
for name in sorted(expected - set(notes)):
    errors.append("Declared note not found: " + name)

def check_target(name, p, target, wiki=False):
    target = unquote(target.split("|", 1)[0].split("#", 1)[0].strip().strip("<>"))
    if not target or urlsplit(target).scheme:
        return
    if wiki:
        candidate = (ROOT / target).with_suffix(".md") if not Path(target).suffix else ROOT / target
    else:
        candidate = p.parent / target
    candidate = candidate.resolve()
    if not candidate.is_relative_to(ROOT) or not candidate.exists():
        errors.append(name + ": broken/local-external link -> " + target)

for name, p in notes.items():
    source = p.read_text(encoding="utf-8")
    for target in re.findall(r"\[\[([^\]]+)\]\]", source):
        check_target(name, p, target, wiki=True)
    for target in re.findall(r"!?(?<!\[)\[[^\]\n]*\]\(([^)]+)\)", source):
        check_target(name, p, target)
for name in ["README.md", "00_Inicio/Estado Atual.md", "00_Inicio/Historico de Contexto.md"]:
    if name in notes and manifest["context_revision"] not in notes[name].read_text(encoding="utf-8"):
        errors.append("Revision not recorded in " + name)
hashes = {name: hashlib.sha256(p.read_bytes()).hexdigest() for name, p in paths.items()}
if args.refresh and not errors:
    manifest["sha256"] = hashes
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
elif manifest.get("sha256") != hashes:
    errors.append("Hashes changed; review and run --refresh")
initial_names = manifest["entrypoints"] + manifest["current"]
metrics = {
    "notes_total": len(notes),
    "initial_notes": len(initial_names),
    "initial_characters": sum(len(paths[n].read_text(encoding="utf-8")) for n in initial_names if n in paths),
    "initial_utf8_bytes": sum(paths[n].stat().st_size for n in initial_names if n in paths),
}
print(json.dumps({"ok": not errors, "revision": manifest["context_revision"],
                  "metrics": metrics, "errors": errors}, ensure_ascii=True, indent=2))
sys.exit(1 if errors else 0)
