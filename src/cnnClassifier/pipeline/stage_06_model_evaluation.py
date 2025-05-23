from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation import ModelEvaluation
from cnnClassifier import logger


STAGE_NAME = "Evaluation stage"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = ModelEvaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == '__main__':
    try:
        logger.info("*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
