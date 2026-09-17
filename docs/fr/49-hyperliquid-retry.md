# 49 — Retries et erreurs partielles

**Source :** `prototype/hyperliquid_reconciliation.py`.

Ce chapitre isole la reprise ciblée. les erreurs transitoires sont séparées des erreurs définitives avant nouvelle tentative. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Un retry global peut dupliquer une action déjà exécutée. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Trace AIR et contraintes locales](50-zk-air.md)._
