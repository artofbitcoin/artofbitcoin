# 53 — Propriété de liaison

**Source :** `prototype/zk_commitment.py`.

Ce chapitre isole la liaison entre message et engagement. le vérificateur attend le même encodage canonique lors de l’ouverture. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Les conversions implicites d’entiers ou de tableaux doivent être interdites. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Vérificateur de preuve](54-zk-verifier.md)._
