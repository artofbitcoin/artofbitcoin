# artofbitcoin

Exploration technique de Bitcoin, des preuves zero-knowledge et des infrastructures blockchain.
Je construis une bibliothèque francophone fondée sur la lecture du code source : architecture, invariants de sécurité, compromis et limites opérationnelles.

## Axes de travail

- **Bitcoin** — protocoles, signatures, scripts et outils de l'écosystème.
- **ZK / zkVM** — STARK, AIR, FRI, récursion et enveloppes SNARK.
- **Confidentialité** — FHE, permissions de déchiffrement et calcul sur données chiffrées.
- **Layer 2** — contrats système, messagerie et bridges de Base.
- **Hyperliquid / HyperEVM** — reconstruction du carnet, Bridge2 et sécurité des signatures.

## Parcours techniques récents

- [SP1](https://github.com/artofbitcoin/sp1/tree/main/docs/fr) — zkVM RISC-V, AIR, FRI, récursion et vérification SNARK.
- [CoFHE MiniApp](https://github.com/artofbitcoin/cofhe-miniapp-template/tree/master/docs/fr) — FHE, contrôle d'accès et intégration Base.
- [Base Contracts](https://github.com/artofbitcoin/contracts/tree/main/docs/fr) — dépôts, retraits, pont de jetons et gouvernance.
- [Hyperliquid Order Book Server](https://github.com/artofbitcoin/order_book_server/tree/main/docs/fr) — instantanés, différences L4 et cohérence locale.
- [HyperEVM Contracts](https://github.com/artofbitcoin/hyperliquid-contracts/tree/master/docs/fr) — bridge, séparation de domaines et protection contre le rejeu.

## Méthode

Chaque parcours est découpé en chapitres courts et traçables, un mécanisme par commit. Les observations sont reliées aux fichiers et aux tests du dépôt ; elles ne prétendent ni remplacer un audit, ni certifier un déploiement.
