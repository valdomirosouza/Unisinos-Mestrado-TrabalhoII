#!/usr/bin/env python3
"""Ingere um PDF baixado (~/Downloads) para docs/ com o nome canônico do estudo.

Fluxo do ciclo: baixar o PDF pelo proxy CAPES → `ingest-downloads.py P97` —
o script pega o PDF **mais recente** de ~/Downloads, valida o magic %PDF,
move para docs/P97_<slug-do-título>.pdf e atualiza a coluna
"File name (folder: docs)" do Papers_Index.csv (apenas se estava PENDENTE).

Uso:
  ingest-downloads.py <PID>            ingere o PDF mais recente para o PID
  ingest-downloads.py <PID> <arquivo>  ingere um arquivo específico
  ingest-downloads.py --list           lista os PIDs ainda pendentes
"""
import csv
import re
import sys
import time
from pathlib import Path

INDEX = Path(__file__).resolve().parent.parent / 'Papers_Index.csv'
DOCS = INDEX.parent / 'docs'
DOWNLOADS = Path.home() / 'Downloads'
FILECOL = 'File name (folder: docs)'


def load():
    with open(INDEX, encoding='utf-8') as fh:
        r = csv.DictReader(fh)
        return r.fieldnames, list(r)


def save(cols, rows):
    with open(INDEX, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)


def slug(t: str) -> str:
    return re.sub(r'[^A-Za-z0-9]+', '_', t).strip('_')[:80]


def main() -> int:
    cols, rows = load()
    if len(sys.argv) > 1 and sys.argv[1] == '--list':
        pend = [r for r in rows if r[FILECOL].startswith('PENDENTE')]
        for r in pend:
            print(f"{r['Paper ID']}  {r['title'][:70]}")
        print(f'{len(pend)} pendentes')
        return 0
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    pid = sys.argv[1].upper()
    row = next((r for r in rows if r['Paper ID'] == pid), None)
    if row is None:
        print(f'{pid} não existe no índice', file=sys.stderr)
        return 1

    if len(sys.argv) > 2:
        src = Path(sys.argv[2]).expanduser()
    else:
        pdfs = sorted(DOWNLOADS.glob('*.pdf'), key=lambda p: p.stat().st_mtime, reverse=True)
        if not pdfs:
            print(f'nenhum PDF em {DOWNLOADS}', file=sys.stderr)
            return 1
        src = pdfs[0]
        age = time.time() - src.stat().st_mtime
        print(f'mais recente: {src.name} ({age:.0f}s atrás)')
        if age > 600:
            print('AVISO: arquivo tem mais de 10 min — confirme que é o certo '
                  '(passe o caminho explicitamente para forçar)', file=sys.stderr)
            return 1

    data = src.read_bytes()
    if data[:5] != b'%PDF-':
        print(f'{src} não é um PDF válido', file=sys.stderr)
        return 1

    dest = DOCS / f'{pid}_{slug(row["title"])}.pdf'
    if dest.exists():
        print(f'{dest.name} já existe — não sobrescrevo', file=sys.stderr)
        return 1
    dest.write_bytes(data)
    src.unlink()

    if row[FILECOL].startswith('PENDENTE') or not row[FILECOL].strip():
        row[FILECOL] = dest.name
        save(cols, rows)
        print(f'{pid}: {dest.name} ({len(data)//1024} KB) · índice atualizado')
    else:
        print(f'{pid}: {dest.name} salvo; índice já tinha "{row[FILECOL]}" — não alterado')
    print('Lembrete: re-derive o Papers_Index.md ao final '
          '(python3 scripts/derive-index.py --csv Papers_Index.csv --out Papers_Index.md)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
