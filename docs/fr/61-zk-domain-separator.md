# 61 — Séparateur de domaine ZK

**Source :** `prototype/zk_domain_separator.py`.

Ce chapitre isole la séparation cryptographique des contextes. le séparateur lie message, circuit et application avant de produire ou vérifier un engagement. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Réutiliser un transcript dans un autre domaine annule la séparation attendue. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Échecs explicites du vérificateur ZK](62-zk-verifier-failure.md)._
