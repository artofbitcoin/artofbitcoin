# 08 — Échecs déterministes de Script

**Source :** `prototype/bitcoin_script_opcode_trace.py`.

Ce chapitre isole la classification des échecs. les erreurs de pile, d’encodage et de condition sont séparées dans le diagnostic. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Transformer toute erreur en false sans contexte rend les audits de transaction opaques. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Profondeur de confirmation](09-bitcoin-confirmation.md)._
