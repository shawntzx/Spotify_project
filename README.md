<!-- Overview -->
## Spotify Automated ETL Pipeline and Tracks Recommendations

Stage 1:

* Develop an automated ETL pipeline locally using DAGs and Airflow to extract user play history from spotify API
* Deploy the pipeline on Azure using Data Factory with Azure Databricks and FunctionApp

Stage 2:

* Perform data analysis on past tracks played history
* Build a model to make recommendations based on tracks played history

<!-- Progress -->
## Progress

First stage is completed. Currently work on second stage development. 

In stage 1 local ETL pipeline, it extracts data from spotify api, tranform data locally and store the in local SQLite database. 

Next, the pipeline is deployed on Azure. Data Factory is used to orchestrate the pipeline in a similar way as the local development. First step is to extract data from spotify using FunctionApp and a trigger, store the data in one container as the bronze layer. After that, Azure Databricks is used to transform the data, perform data analysis and store in another container as the silver layer. Last step is to build a model to make recommendations. The pipeline is scheduled to run on daily basis automatically. 

<!-- Dependencies -->

### Dependencies can be installed with environment.yml



<!-- CONTACT -->
## Contact

Zixiang Tang - shawntang126@gamil.com

Project Link: [https://github.com/shawntzx/Spotify_project](https://github.com/shawntzx/Spotify_project)

