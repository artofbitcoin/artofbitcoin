# 32 — Anti-rejeu des messages Base

**Source :** `prototype/base_message_replay.py`.

Ce chapitre isole la consommation d’un message. un message possède une identité stable et ne peut être consommé deux fois par la même frontière. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** La vérification et la consommation doivent former une opération cohérente. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Domaine d’un message Base](33-base-message-domain.md)._
