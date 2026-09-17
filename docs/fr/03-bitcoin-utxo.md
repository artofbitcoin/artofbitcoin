# 03 — Modèle UTXO et consommation

**Source :** `prototype/bitcoin_utxo_validator.py`.

Ce chapitre isole la consommation d’un UTXO. le validateur vérifie qu’une sortie existante est consommée une seule fois et que ses montants restent cohérents. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** La prévention du double spend dépend de l’état observé et de la règle de sélection. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Validation des scripts UTXO](04-bitcoin-utxo-script.md)._
