# Architecture Bitcoin : du consensus à la mempool

Bitcoin sépare la validation des blocs, le modèle UTXO, les scripts de dépense et la propagation réseau. Un nœud conserve des transactions candidates dans la mempool avant leur inclusion dans un bloc.

La finalité observée dépend de la profondeur et des hypothèses de réorganisation. Les signatures autorisent une dépense selon le script ; elles ne garantissent ni l identité juridique du détenteur ni la disponibilité d un service d indexation.

Cette grille distingue consensus, politique locale du nœud et interprétation applicative.
