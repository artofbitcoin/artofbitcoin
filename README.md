# artofbitcoin

### Bitcoin-native thinking for secure onchain systems

Exploration technique de Bitcoin, des preuves zero-knowledge et des infrastructures blockchain. Je construis une bibliothèque francophone fondée sur la lecture du code source : architecture, invariants de sécurité, compromis et limites opérationnelles.

## Axes de travail

- **Bitcoin** — consensus, signatures, scripts, Ordinals, Runes, indexation et mempool.
- **ZK / zkVM** — STARK, AIR, FRI, récursion et enveloppes SNARK.
- **Base** — contrats système, bridges et sponsoring ERC-4337.
- **Hyperliquid / HyperEVM** — carnets, Bridge2, quorums et conservation cross-domain.
- **Confidentialité** — FHE, permissions de déchiffrement et calcul sur données chiffrées.

## Travaux mis en avant

| Domaine | Parcours | Valeur documentée |
| --- | --- | --- |
| Base / ERC-4337 | [Verifying Paymaster](https://github.com/artofbitcoin/verifying-paymaster/tree/master/docs/fr) | Domaine signé, bundlers, paiement ERC-20, griefing et coupe-circuit |
| Hyperliquid | [Hyperliquid Contracts](https://github.com/artofbitcoin/hyperliquid-contracts/tree/master/docs/fr) | Bridge2, quorum, rotation, nonces, solvabilité et réponse aux incidents |
| Hyperliquid data | [Order Book Server](https://github.com/artofbitcoin/order_book_server/tree/main/docs/fr) | Instantanés, différences L4, reconnexion et cohérence locale |
| Base L2 | [Base Contracts](https://github.com/artofbitcoin/contracts/tree/main/docs/fr) | Dépôts, retraits, messagerie, conservation et gouvernance |
| ZK | [SP1](https://github.com/artofbitcoin/sp1/tree/main/docs/fr) | zkVM RISC-V, AIR, FRI, récursion et vérification SNARK |
| FHE sur Base | [CoFHE MiniApp](https://github.com/artofbitcoin/cofhe-miniapp-template/tree/master/docs/fr) | Calcul chiffré, permissions et frontière client/coprocesseur |

## Perspective Bitcoin et actifs représentés

Un actif enveloppé ne reçoit pas la sécurité de Bitcoin par simple déploiement sur une EVM. Mes parcours distinguent systématiquement la finalité de la chaîne source, le modèle de garde ou de preuve du wrapper, la solvabilité du pont et la finalité de la chaîne destination.

## Méthode

Chaque parcours est découpé en chapitres courts et traçables, un mécanisme par commit. Les observations sont reliées aux fichiers et suites de tests du dépôt ; elles ne prétendent ni remplacer un audit, ni certifier un déploiement. Aucun résultat de test n’est revendiqué lorsqu’aucun test n’a été exécuté.
