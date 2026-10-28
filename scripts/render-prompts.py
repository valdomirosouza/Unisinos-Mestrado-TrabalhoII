#!/usr/bin/env python3
"""Renderiza prompts por estudo a partir do template canônico.

Um único template normativo (templates/prompt-avaliacao.md) vira as cópias por
estudo em prompts/prompt-PXX.md, preenchendo os marcadores {{...}} com os dados
do índice canônico. Elimina a classe de divergência em que um avaliador recebe
texto normativo diferente dos demais (worked example: família B, 3/8 divergências).

Uso:
  render-prompts.py --index Papers_Index.csv --ids P43,P44 \
      [--template templates/prompt-avaliacao.md] [--outdir prompts] \
      [--emendas "PDR-0002: ..."] [--dry-run]
"""
import argparse
import csv
import re
import sys
from pathlib import Path

FIELD_MAP = {  # marcador -> coluna do índice (ajustado à instância: Papers_Index.csv)
    'PAPER_ID': 'Paper ID', 'TITULO': 'title', 'ANO': 'year',
    'VEICULO': 'venue', 'DOI': 'doi', 'CIT': 'citations (2026-09-06)',
    'CIT_OA': 'citations_openalex', 'CIT_CR': 'citations_crossref',
    'CIT_SC': 'citations_scopus',
    'QUALIS': 'Scopus (Percentil)', 'SJR': 'SJR Quartile',
    'ARQUIVO_PDF': 'File name (folder: docs)',
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--index', required=True)
    ap.add_argument('--ids', required=True, help='lista separada por vírgula, ex.: P43,P44')
    ap.add_argument('--template', default='templates/prompt-avaliacao.md')
    ap.add_argument('--outdir', default='prompts')
    ap.add_argument('--emendas', default='(nenhuma emenda vigente)')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    template = Path(args.template).read_text(encoding='utf-8')
    with open(args.index, encoding='utf-8') as fh:
        rows = {r[FIELD_MAP['PAPER_ID']]: r for r in csv.DictReader(fh)}

    wanted = [i.strip() for i in args.ids.split(',')]
    missing = [i for i in wanted if i not in rows]
    if missing:
        print(f'IDs ausentes do índice: {missing}', file=sys.stderr)
        return 1

    outdir = Path(args.outdir)
    outdir.mkdir(exist_ok=True)
    for pid in wanted:
        row = rows[pid]
        text = template
        for marker, col in FIELD_MAP.items():
            text = text.replace('{{%s}}' % marker, str(row.get(col, '')).strip() or 'N/D')
        text = text.replace('{{EMENDAS_NORMATIVAS}}', args.emendas)
        text = text.replace('{{RESSALVAS_TRIAGEM}}', row.get('ressalvas', '') or 'nenhuma')
        leftover = sorted(set(re.findall(r'\{\{([A-Z_0-9]+)\}\}', text)))
        if leftover:
            print(f'{pid}: marcadores não resolvidos (preencher na instância): {leftover}')
        out = outdir / f'prompt-{pid}.md'
        if args.dry_run:
            print(f'[dry-run] escreveria {out}')
        else:
            out.write_text(text, encoding='utf-8')
            print(f'escrito {out}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
