# 33 — Domaine d’un message Base

**Source :** `prototype/base_message_replay.py`.

Ce chapitre isole la séparation source-destination. la clé du message inclut les domaines afin qu’une preuve d’une chaîne ne soit pas réutilisée sur une autre. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Omettre la destination ouvre une substitution de contexte. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Reprise d’un relai Base](34-base-message-recovery.md)._
