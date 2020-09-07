# DataServices-Composition
An implementation of our quality-driven service selection and composition approach, to identify and compose the relevant data services that can be used to leverage the missing information, and to select the best-quality query plans for the enrichment of users data sources. Specifically, we made the following contributions:

– An algorithm for reformulating queries expressed over the schema of the user data source by replacing the missing concepts in the user data source with
invocations to data services. This algorithm adapts existing Local-As-View query reformulation algorithms.

– A knapsack-based algorithm for the selection of the query plans (and therefore the pertinent data services), taking into account the quality of the
services, the time and monetary cost limits set by the user

The main file is: EuDaSL.py

Three fields must be specified, data queries, the cost threshold and the response time not to exceed.

Three selection methods are supported:

1. Optimal Query Plan Selection

2. Knapsack based Selection method

3. Selection of all the possible Query Plans.

The selection of plans involves multiple criteria (i.e., different QoS criteria). The idea is to associate an aggregated quality score to each executable query plan in order to be able to compare and rank different plans. This problem, from the multi-criteria perspective, can be solved using the Simple Additive Weighting (SAW)  method. SAW formules are defined in the file formules_saw.py

The file quality_score.py contains all the required methods for the evaluation of QoS values of composite service executions such as the execution cost, the service reputation, its availability, its reliability and the estimated response time. 

The performance of our system is evaluated using publicly available DP services, that export rich information about different domains (e.g., information about books, authors, music, albums, movies and videos, etc.). In particular, we refer to DP services provided by the following websites: LibraryThing, Isbndb, AdeBooks, IVA, LastFM, MusicBrainz, Discogs, MusixMatch, Spotify, IMDb and Amazon.

The file Service_lake contains the definition of the data services we make use of.

The file defuse.py contains the implementation of our selection algorithms. 

The file knapsack01.py implements a dynamic programming solution for the selection of the query plans (and therefore the DP-Services), taking into account the quality of the services and the time and monetary cost limits set by the user
