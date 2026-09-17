# 16 — Frais et monnaie rendue

**Source :** `prototype/bitcoin_fee_estimator.py`.

Ce chapitre isole le calcul de la monnaie. le calcul sépare montant envoyé, frais et sortie de retour afin de contrôler la conservation. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Une sortie de poussière ou un débordement doit être traité explicitement. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Frais et politique de confirmation](17-bitcoin-fees-policy.md)._
