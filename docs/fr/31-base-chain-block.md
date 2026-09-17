# 31 — Bloc et séquence Base

**Source :** `prototype/base_chain_context.py`.

Ce chapitre isole la cohérence du bloc. les champs de bloc servent à comparer des observations prises dans un même contexte. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Comparer des données de hauteurs différentes crée des faux écarts. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Anti-rejeu des messages Base](32-base-message-replay.md)._
