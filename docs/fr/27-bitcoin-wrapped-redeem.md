# 27 — Rachat d’un actif enveloppé

**Source :** `docs/bitcoin-wrapped-asset-security.md`.

Ce chapitre isole la conversion retour. le rachat relie une demande destination à une dépense ou libération vérifiable côté source. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Les files d’attente et échecs de relai doivent rester observables. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Invariant de solvabilité d’un wrapper](28-bitcoin-wrapped-invariant.md)._
