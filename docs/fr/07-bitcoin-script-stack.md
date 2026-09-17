# 07 — Pile et éléments témoins

**Source :** `prototype/bitcoin_script_opcode_trace.py`.

Ce chapitre isole la discipline de pile. les opcodes transforment une pile bornée ; l’ordre des éléments fait partie du contrat du script. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Une représentation simplifiée de la pile peut masquer une différence de sémantique. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Échecs déterministes de Script](08-bitcoin-script-failure.md)._
