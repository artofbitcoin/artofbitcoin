# 17 — Frais et politique de confirmation

**Source :** `prototype/bitcoin_fee_estimator.py`.

Ce chapitre isole le lien entre coût et délai. la politique relie le niveau de frais à une priorité sans confondre recommandation et consensus. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Le marché des frais change ; une valeur figée devient vite obsolète. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Dépendances dans le mempool](18-bitcoin-mempool-dependency.md)._
