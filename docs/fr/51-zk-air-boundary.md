# 51 — Contraintes de bord AIR

**Source :** `prototype/zk_trace_air.py`.

Ce chapitre isole les états initial et final. les contraintes de bord relient la trace au calcul attendu avant toute composition. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Une trace localement cohérente peut être globalement fausse sans ancrage. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Engagement de preuve ZK](52-zk-commitment.md)._
