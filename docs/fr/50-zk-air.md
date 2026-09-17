# 50 — Trace AIR et contraintes locales

**Source :** `prototype/zk_trace_air.py`.

Ce chapitre isole les relations de transition. la trace ZK encode des états et des contraintes locales vérifiables. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Une contrainte manquante laisse une transition invalide hors du contrôle. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Contraintes de bord AIR](51-zk-air-boundary.md)._
