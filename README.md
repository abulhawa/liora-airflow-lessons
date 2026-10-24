# Liora Airflow lessons

Airflow lesson exercises developed on a course VM in the `airflow_dst` folder.

- `dags/my_first_dag.py`: first Python tasks and task ordering.
- `dags/leaving_home_dag.py`: dependencies between getting-ready tasks.
- `dags/scheduling_dags.py`: a DAG scheduled every minute.
- `docker-compose.yaml`: lesson setup based on the Apache Airflow example.

The Compose file is a learning setup with example default credentials, intended for a course environment. Local environment values, generated configuration, logs, caches and database state are excluded. Configure these separately to run the exercises.

## Saving work

On the VM:

```bash
cd ~/airflow_dst
git status
git add dags docker-compose.yaml README.md .gitignore
git commit -m "Describe the lesson changes"
```

Then run the laptop bridge script `sync-airflow.ps1` to fetch VM commits and push to GitHub. GitHub authentication stays on the laptop.
