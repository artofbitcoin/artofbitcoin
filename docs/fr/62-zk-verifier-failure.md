# 62 — Échecs explicites du vérificateur ZK

**Source :** `prototype/zk_proof_verifier.py`.

Ce chapitre isole la classification des rejets. le vérificateur distingue preuve mal formée, entrée incohérente et paramètre de domaine incorrect. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Masquer la cause du rejet ralentit le diagnostic et peut favoriser un fallback dangereux. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Index](63-index.md)._
