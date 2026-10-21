#!/usr/bin/env bash
# Packs pack/ into dist/create-green-signals-<version>.zip (pack.mcmeta at zip root).
set -euo pipefail
VERSION="${1:-1.0.0}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/dist/create-green-signals-$VERSION.zip"
mkdir -p "$ROOT/dist"
rm -f "$OUT"
(cd "$ROOT/pack" && python3 -m zipfile -c "$OUT" *)
echo "built $OUT"
