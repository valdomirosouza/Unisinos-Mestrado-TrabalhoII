#!/usr/bin/env python3
"""Confiabilidade inter-avaliadores a partir do CSV de comparação.

Calcula, sobre a decisão colapsada Incluir/Excluir: acordo percentual e Cohen's
kappa por par, Fleiss' kappa dos três, prevalência de Incluir e diferenças
médias absolutas de SCORE_RQ/SCORE_QA (pares com NA excluídos) — exatamente a
leitura usada no worked example (91,8% de acordo podia conviver com kappa 0,51
pelo paradoxo da prevalência; reporte os dois).

Regra de colapso: recomendação que começa com "incluir" ou "mantido"
(case-insensitive) = Incluir; qualquer outra = Excluir.

Uso: compute-kappa.py --csv reviews/comparacao-avaliadores.csv \
        [--evaluators Aval1,Aval2,Aval3]

Os nomes passados em --evaluators devem prefixar as colunas do CSV
(<Nome>_RQ, <Nome>_QA, <Nome>_Rec).
"""
import argparse
import csv
import itertools
import statistics
import sys



def collapse(rec: str) -> str:
    r = rec.strip().lower()
    return 'I' if (r.startswith('incluir') or r.startswith('mantido')) else 'E'


def cohen(a, b):
    po = sum(x == y for x, y in zip(a, b)) / len(a)
    pe = sum((a.count(c) / len(a)) * (b.count(c) / len(b)) for c in 'IE')
    return po, (po - pe) / (1 - pe) if pe < 1 else float('nan')


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--csv', required=True)
    ap.add_argument('--evaluators', default='Aval1,Aval2,Aval3',
                    help='nomes que prefixam as colunas <Nome>_RQ/_QA/_Rec')
    args = ap.parse_args()
    EVAL = [e.strip() for e in args.evaluators.split(',')]
    with open(args.csv, encoding='utf-8') as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        print('CSV vazio', file=sys.stderr)
        return 1

    dec = {e: [collapse(r[f'{e}_Rec']) for r in rows] for e in EVAL}
    allv = sum(dec.values(), [])
    print(f'n = {len(rows)} decisões · prevalência Incluir: '
          f'{allv.count("I")}/{len(allv)} = {allv.count("I")/len(allv)*100:.1f}%')

    for x, y in itertools.combinations(EVAL, 2):
        po, k = cohen(dec[x], dec[y])
        print(f'{x}×{y}: acordo {po*100:.1f}% · Cohen κ = {k:.2f}')

    counts = [[sum(1 for e in EVAL if dec[e][i] == c) for c in 'IE'] for i in range(len(rows))]
    n_rat = len(EVAL)
    p_bar = statistics.mean((sum(c * c for c in row) - n_rat) / (n_rat * (n_rat - 1)) for row in counts)
    pj = [sum(row[j] for row in counts) / (len(rows) * n_rat) for j in range(2)]
    pe = sum(p * p for p in pj)
    print(f'Fleiss κ (3 avaliadores) = {(p_bar - pe)/(1 - pe):.2f}')

    unan = sum(1 for i in range(len(rows)) if len({dec[e][i] for e in EVAL}) == 1)
    div = [rows[i].get('ID', str(i)) for i in range(len(rows)) if len({dec[e][i] for e in EVAL}) > 1]
    print(f'unânimes: {unan}/{len(rows)} · divergências: {div or "nenhuma"}')

    for metric in ('RQ', 'QA'):
        for x, y in itertools.combinations(EVAL, 2):
            vals = [abs(float(r[f'{x}_{metric}']) - float(r[f'{y}_{metric}']))
                    for r in rows if r[f'{x}_{metric}'] not in ('NA', '') and r[f'{y}_{metric}'] not in ('NA', '')]
            if vals:
                print(f'|Δ{metric}| {x}×{y}: {statistics.mean(vals):.2f} (n={len(vals)})')
    return 0


if __name__ == '__main__':
    sys.exit(main())
