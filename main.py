from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from cnnClassifier.pipeline.stage_03_data_transformation import DataTransformationPipeline
from cnnClassifier.pipeline.stage_04_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_05_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_06_evaluation import ModelEvaluationPipeline
from cnnClassifier import logger


def run_pipeline_stage(stage_name: str, pipeline_cls):
    try:
        logger.info(f"\n\n================== {stage_name} started ==================")
        pipeline = pipeline_cls()
        pipeline.main()
        logger.info(f"================== {stage_name} completed ==================\n")
    except Exception as e:
        logger.exception(f"Exception in stage: {stage_name}")
        raise e


if __name__ == "__main__":
    run_pipeline_stage("STAGE 01 - Data Ingestion", DataIngestionTrainingPipeline)
    run_pipeline_stage("STAGE 02 - Data Validation", DataValidationTrainingPipeline)
    run_pipeline_stage("STAGE 03 - Data Transformation", DataTransformationPipeline)
    run_pipeline_stage("STAGE 04 - Prepare Base Model", PrepareBaseModelTrainingPipeline)
    run_pipeline_stage("STAGE 05 - Model Training", ModelTrainingPipeline)
    run_pipeline_stage("STAGE 06 - Model Evaluation", ModelEvaluationPipeline)
