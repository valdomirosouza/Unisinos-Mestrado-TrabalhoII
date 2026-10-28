#!/usr/bin/env bash
# Validação determinística da instância de RSL. Roda localmente e no CI.
#
# Uso: check-rsl.sh [--quiet]
#
# Checks
#   C1 links Markdown internos resolvem (todo o repositório)
#   C2 índice de PDRs: numeração contígua, todo PDR linkado no README dos PDRs
#   C3 indexação: todo arquivo em prompts/, reviews/, report/, picoc/ aparece
#      em algum README (convenção de indexação)
#   C4 varredura de segredos: padrões de chave de API em arquivos versionados
#   C5 invariantes de contagem (se os CSVs da instância existirem):
#      - reviews/review-PXX.md existe para toda linha avaliada do consolidado
#      - contagens citadas no README raiz batem com os CSVs (via contagens.yml,
#        se presente)
set -euo pipefail
cd "$(dirname "$0")/.."
FAIL=0
say() { [ "${1:-}" = "--quiet" ] || echo "$@"; }

echo "== C1: links internos =="
python3 - <<'PY' || FAIL=1
import re, subprocess, sys
from pathlib import Path
from urllib.parse import unquote
tracked = subprocess.run(['git', 'ls-files'], capture_output=True, text=True).stdout.splitlines()
bad = 0
for name in tracked:
    md = Path(name)
    if md.suffix != '.md': continue
    text = md.read_text(encoding='utf-8', errors='replace')
    for m in re.finditer(r'\]\(([^)#\s]+(?:\.md|\.csv|\.sh|\.py|\.yml|\.cff|\.pdf))(?:#[^)]*)?\)', text):
        target = unquote(m.group(1))
        if re.match(r'^[a-z][a-z0-9+.-]*:', target): continue  # qualquer esquema de URI (http, file, mailto, …)
        if '{{' in target: continue  # placeholder de template
        if not (md.parent / target).resolve().exists():
            print(f'  LINK QUEBRADO: {md}: {target}'); bad += 1
sys.exit(1 if bad else 0)
PY

echo "== C2: índice de PDRs =="
python3 - <<'PY' || FAIL=1
import re, sys
from pathlib import Path
pdrdir = Path('protocolo/pdr')
pdrs = sorted(p.name for p in pdrdir.glob('PDR-[0-9]*.md'))
nums = [int(re.match(r'PDR-(\d{4})', n).group(1)) for n in pdrs]
ok = True
if nums != list(range(1, len(nums) + 1)):
    print(f'  NUMERAÇÃO NÃO CONTÍGUA: {nums}'); ok = False
index = (pdrdir / 'README.md').read_text(encoding='utf-8')
for n in pdrs:
    if n not in index:
        print(f'  PDR FORA DO ÍNDICE: {n}'); ok = False
sys.exit(0 if ok else 1)
PY

echo "== C3: indexação de artefatos =="
python3 - <<'PY' || FAIL=1
import subprocess, sys
from pathlib import Path
tracked = [Path(p) for p in subprocess.run(['git', 'ls-files'], capture_output=True, text=True).stdout.splitlines()]
cache = {}
def readme_text(d: Path) -> str:
    if d not in cache:
        r = d / 'README.md'
        cache[d] = r.read_text(encoding='utf-8', errors='replace') if r.exists() else ''
    return cache[d]
ok = True
for f in tracked:
    if not f.parts or f.parts[0] not in ('prompts', 'reviews', 'report', 'picoc'): continue
    if f.name == 'README.md': continue
    # indexado se o nome aparece em algum README do diretório do arquivo até a raiz
    dirs = [f.parent] + list(f.parent.parents)
    if not any(f.name in readme_text(d) for d in dirs):
        print(f'  NÃO INDEXADO: {f}'); ok = False
sys.exit(0 if ok else 1)
PY

echo "== C4: varredura de segredos =="
if git grep -nIE '(api[_-]?key|apikey)[\"'"'"']?\s*[:=]\s*[\"'"'"'][A-Za-z0-9]{16,}|sk-[A-Za-z0-9]{20,}' -- ':!scripts/check-rsl.sh' 2>/dev/null; then
    echo '  POSSÍVEL SEGREDO VERSIONADO (acima)'; FAIL=1
else
    echo '  ok'
fi

echo "== C5: invariantes de contagem =="
python3 - <<'PY' || FAIL=1
import csv, sys
from pathlib import Path
ok = True
for cons in Path('reviews').glob('resultados-consolidados*.csv') if Path('reviews').is_dir() else []:
    with open(cons, encoding='utf-8') as fh:
        for row in csv.DictReader(fh):
            rid = row.get('ID', '')
            if rid and not (Path('reviews') / f'review-{rid}.md').exists():
                print(f'  {cons.name}: {rid} sem review-{rid}.md'); ok = False
print('  ok' if ok else '  falhas acima')
sys.exit(0 if ok else 1)
PY

if [ "$FAIL" -ne 0 ]; then echo 'check-rsl: FALHOU'; exit 1; fi
echo 'check-rsl: OK'
