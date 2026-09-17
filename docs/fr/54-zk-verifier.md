# 54 — Vérificateur de preuve

**Source :** `prototype/zk_proof_verifier.py`.

Ce chapitre isole la vérification des assertions. le vérificateur sépare preuve, entrées publiques et paramètres de domaine. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Accepter des paramètres provenant d’un autre circuit casse la frontière de confiance. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Décision de politique FHE](55-fhe-policy.md)._
