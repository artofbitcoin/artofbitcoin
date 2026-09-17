# 43 — Nonce signé Hyperliquid

**Source :** `prototype/hyperliquid_signed_nonce.py`.

Ce chapitre isole le nonce et le domaine signé. le nonce lie la demande à son compte et à son contexte d’exécution. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Un nonce partagé entre flux facilite les collisions et les rejouements. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Domaine d’une signature Hyperliquid](44-hyperliquid-domain.md)._
