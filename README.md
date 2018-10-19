# Semantix Test
This repository is a challenge sended by Semantix.
The objective of this challenge, is analyse and extract information from [NASA request datasetl](http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html).
There is two datasets on this link, i opted to handle one by execution. So, if wich to execute the
script to check results from both, stay tuned on 'results' folder, because all folders and files there
can be overwritten.


### Installation

Once you have cloned this repository, you just need to install [Docker](https://docs.docker.com/install/]) and [Docker Compose](https://docs.docker.com/compose/).

After intall and configure Docker, you should run:

```
docker-compose run --rm ps bash
```
or
```
dcr --rm ps bash
```
If you dont use OH-MY-ZSH with docker compose plugin, the firt one will not work.


### Execution


Once you are in docker bash opened by the last command, you should run:

```
$SPARK_HOME/bin/spark-submit nasa_analysis_df.py data/NASA_access_log_Aug95
```

In my case, i have a folder `data` inside my project. But, you can give a path from another place, for example:

```
$SPARK_HOME/bin/spark-submit nasa_analysis_df.py ../foo/bar/NASA_access_log_Aug95
```

When the execution finishes, it creates a folder `results` where for each informantion a subfolder with a .CSV  is created inside.

It should create this folders inside `results`:

  - `bytes_per_day` -> (Quantity of Bytes per day.)
  - `frequency_status` -> (Frequency of each http status)
  - qty_http_404_per_day -> (Quantity of http 404 per Day)
  - sum_bytes -> (Sum of all request bytes)
  - `top_20_request` -> (Top twenty requests)
  - top_5_hosts_http_404 -> (Top five hosts with response http 404)
  - total_http_404 -> (Total of http 404)
  - unique_hosts -> (List of unique hosts)

In red, are informations that did not belongs to the challenge, but its a plus.

Also, there is some questions on the Test. To see this go to TEST_ANSWERS.md. Those answers are in PT-BR because the test is in PT-BR.

I hope you liked.
Feel free to create a issue, if you want.

Regards.




