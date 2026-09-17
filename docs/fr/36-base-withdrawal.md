# 36 — Retrait depuis Base

**Source :** `prototype/base_deposit_withdrawal.py`.

Ce chapitre isole la demande de retrait. la demande est liée au bénéficiaire et à la quantité avant d’entrer dans la file de règlement. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Une modification du bénéficiaire après signature doit invalider la demande. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Comptabilité du bridge Base](37-base-bridge-accounting.md)._
