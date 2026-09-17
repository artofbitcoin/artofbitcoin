# 10 — Politique d’acceptation des confirmations

**Source :** `prototype/bitcoin_confirmation_depth.py`.

Ce chapitre isole le seuil métier. l’application choisit un seuil selon la valeur, le risque et le type d’opération. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Un seuil unique ne couvre pas tous les scénarios de règlement. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Détection d’une réorganisation](11-bitcoin-reorg.md)._
