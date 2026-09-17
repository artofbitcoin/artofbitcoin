# 44 — Domaine d’une signature Hyperliquid

**Source :** `prototype/hyperliquid_signed_nonce.py`.

Ce chapitre isole la séparation des environnements. le message signé inclut le domaine attendu pour empêcher sa réutilisation ailleurs. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Une signature valide mathématiquement peut rester invalide pour l’application visée. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Fenêtre anti-rejeu Hyperliquid](45-hyperliquid-replay.md)._
