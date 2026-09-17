# 35 — Dépôt vers Base

**Source :** `prototype/base_deposit_withdrawal.py`.

Ce chapitre isole la séquence de dépôt. le flux décrit l’entrée source, le message et le crédit destination comme des états différents. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Le crédit ne doit pas être annoncé avant la preuve de réception attendue. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Retrait depuis Base](36-base-withdrawal.md)._
