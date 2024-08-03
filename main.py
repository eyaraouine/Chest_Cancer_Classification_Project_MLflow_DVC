from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.data_ingestion_stage_01 import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.prepare_base_cnn_model_stage_02 import PrepareBaseModelTrainingPipeline



STAGE_NAME = "Data Ingestion stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(f"Exception occurred during {STAGE_NAME}: {str(e)}")
    raise e



STAGE_NAME = "Prepare base CNN model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
