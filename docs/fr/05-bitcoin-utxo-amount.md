# 05 — Conservation des montants UTXO

**Source :** `prototype/bitcoin_utxo_validator.py`.

Ce chapitre isole la conservation entrée-sortie. le contrôle compare les montants consommés, créés et les frais implicites. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Les unités et bornes entières doivent être explicites pour éviter les arrondis dangereux. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Trace d’opcodes Bitcoin Script](06-bitcoin-script-trace.md)._
