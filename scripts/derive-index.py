#!/usr/bin/env python3
"""Deriva a versão Markdown legível do índice canônico (CSV -> MD).

O CSV é a fonte de verdade (Constituição, Art. VII); o MD é derivado e nunca
editado à mão. Rode após toda mudança no CSV.

Uso: derive-index.py --csv Papers_Index.csv --out Papers_Index.md [--cols "Paper ID,title,year,status_rsl"]
"""
import argparse
import csv
import sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--csv', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--cols', default='', help='subconjunto de colunas, na ordem desejada')
    args = ap.parse_args()

    with open(args.csv, encoding='utf-8') as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        print('CSV vazio', file=sys.stderr)
        return 1
    cols = [c.strip() for c in args.cols.split(',') if c.strip()] or list(rows[0].keys())

    lines = [
        f'# Índice de estudos — derivado de `{Path(args.csv).name}`',
        '',
        '> Gerado por `scripts/derive-index.py`. **Não edite à mão** — edite o CSV e re-derive.',
        '',
        '| ' + ' | '.join(cols) + ' |',
        '| ' + ' | '.join('---' for _ in cols) + ' |',
    ]
    for r in rows:
        lines.append('| ' + ' | '.join(str(r.get(c, '')).replace('|', '\\|') for c in cols) + ' |')
    Path(args.out).write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'{args.out}: {len(rows)} linhas, {len(cols)} colunas')
    return 0


if __name__ == '__main__':
    sys.exit(main())
