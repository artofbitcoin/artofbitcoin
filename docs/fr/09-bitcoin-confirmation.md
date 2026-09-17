# 09 — Profondeur de confirmation

**Source :** `prototype/bitcoin_confirmation_depth.py`.

Ce chapitre isole la profondeur comme signal de finalité. le modèle compte les blocs construits au-dessus d’une transaction pour qualifier son degré de confirmation. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** La profondeur n’est pas une garantie absolue contre une réorganisation. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Politique d’acceptation des confirmations](10-bitcoin-confirmation-policy.md)._
