# 04 — Validation des scripts UTXO

**Source :** `prototype/bitcoin_utxo_validator.py`.

Ce chapitre isole la relation entre script et dépense. la dépense est acceptée seulement si l’entrée satisfait le verrouillage de la sortie précédente. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Une signature valide ne compense pas un script ou un contexte de dépense incorrect. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Conservation des montants UTXO](05-bitcoin-utxo-amount.md)._
