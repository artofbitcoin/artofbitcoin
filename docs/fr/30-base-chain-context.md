# 30 — Contexte de chaîne Base

**Source :** `prototype/base_chain_context.py`.

Ce chapitre isole l’identification du réseau. le prototype lie l’action au chain ID et au contexte de bloc avant d’évaluer sa validité. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Une configuration de test réutilisée en production peut viser le mauvais domaine. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Bloc et séquence Base](31-base-chain-block.md)._
