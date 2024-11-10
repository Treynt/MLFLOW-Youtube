import mlflow
from mlflow_utils import create_mlflow_experiment

if __name__ == "__main__":
    #experiment_id = mlflow.create_experiment(
    #    name="testing_mlflow1",
    #    artifact_location="testing_mlflow1_artifacts",
      #  tags={"env": "dev", "version": "1.0.0"},
    #)
    
    #with mlflow.start_run(experiment_id=experiment_id):
        # Aqui você pode registrar algum parâmetro, métrica, ou artefato para gerar `mlruns`
    #    mlflow.log_param("param1", 5)
    #    mlflow.log_metric("metric1", 0.85)

    experiment_id = create_mlflow_experiment(experiment_name="testing_mlflow2", artifact_location="esting_mlflow2_artifacts", tags={"env": "dev", "version": "1.0.0"})
    print(experiment_id)