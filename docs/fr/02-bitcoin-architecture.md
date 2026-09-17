# 02 — Architecture d’un nœud Bitcoin

**Source :** `docs/bitcoin-architecture.md`.

Ce chapitre isole les couches réseau, validation, stockage et politique. l’architecture distingue réception des transactions, validation, construction des blocs et persistance de l’état. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Une vue applicative ne doit pas être prise pour le consensus lui-même. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Modèle UTXO et consommation](03-bitcoin-utxo.md)._
