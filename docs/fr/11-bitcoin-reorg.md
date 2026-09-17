# 11 — Détection d’une réorganisation

**Source :** `prototype/bitcoin_reorg_detector.py`.

Ce chapitre isole la comparaison de chaînes concurrentes. le détecteur compare ancêtres, hauteurs et identifiants de blocs pour repérer un changement de branche. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Un index qui conserve seulement la hauteur peut valider un bloc orphelin. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Reprise après réorganisation](12-bitcoin-reorg-recovery.md)._
