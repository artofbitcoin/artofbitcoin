# 29 — Finalité pratique après une réorganisation

**Source :** `prototype/bitcoin_confirmation_depth.py`.

Ce chapitre isole la combinaison profondeur-risque. la décision de règlement combine profondeur observée et valeur de l’opération plutôt qu’un seuil aveugle. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Une profondeur faible ou un signal de reorg doit maintenir l’état en attente. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Contexte de chaîne Base](30-base-chain-context.md)._
