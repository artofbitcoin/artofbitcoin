# 59 — Finalité d’un message Base

**Source :** `prototype/base_message_replay.py`.

Ce chapitre isole la distinction relayé-finalisé. le message est séparé en états observé, relayé et finalisé avant crédit ou action irréversible. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** La présence d’un événement ne suffit pas à prouver la finalité de la destination. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Réconciliation CoreWriter](60-hyperevm-corewriter-reconciliation.md)._
