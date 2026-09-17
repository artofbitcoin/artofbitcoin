# 06 — Trace d’opcodes Bitcoin Script

**Source :** `prototype/bitcoin_script_opcode_trace.py`.

Ce chapitre isole l’exécution pas à pas des opcodes. la trace conserve la pile, les éléments consommés et le résultat de chaque opération. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Une trace utile doit rendre visibles les erreurs et les limites d’exécution. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Pile et éléments témoins](07-bitcoin-script-stack.md)._
