# 15 — Estimation des frais Bitcoin

**Source :** `prototype/bitcoin_fee_estimator.py`.

Ce chapitre isole la fourchette de frais. le modèle compare taille estimée, priorité et conditions du mempool avant de proposer un niveau de frais. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Une estimation n’est pas une promesse d’inclusion à une hauteur donnée. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Frais et monnaie rendue](16-bitcoin-fees-change.md)._
