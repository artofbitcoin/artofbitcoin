# 39 — Intention CoreWriter

**Source :** `prototype/hyperevm_corewriter.py`.

Ce chapitre isole la construction d’une action. les paramètres sont préparés dans un ordre déterministe avant l’appel de la frontière. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Un encodage différent peut changer l’action sans changer la forme de la transaction. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [État cross-layer HyperEVM](40-hyperevm-cross-layer.md)._
