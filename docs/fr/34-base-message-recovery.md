# 34 — Reprise d’un relai Base

**Source :** `prototype/base_message_replay.py`.

Ce chapitre isole la reprise idempotente. les tentatives du relayer sont rapprochées d’une intention unique et conservent les erreurs. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Une nouvelle tentative doit pouvoir distinguer absence de réponse et exécution déjà finalisée. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Dépôt vers Base](35-base-deposit.md)._
