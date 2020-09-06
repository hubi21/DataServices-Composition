# DataServices-Composition
An implementation of our quality-driven service selection and composition approach, to identify and compose the relevant data services that can be used to leverage the missing information, and to select the best-quality query plans for the enrichment of users data sources. Specifically, we made the following contributions:

– An algorithm for reformulating queries expressed over the schema of the user data source by replacing the missing concepts in the user data source with
invocations to data services. This algorithm adapts existing Local-As-View query reformulation algorithms.

– A knapsack-based algorithm for the selection of the query plans (and therefore the pertinent data services), taking into account the quality of the
services, the time and monetary cost limits set by the user

The main file is: EuDaSL.py
