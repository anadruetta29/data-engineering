from extract import main as extract_main
from transform import main as transform_main
from load import main as load_main


def run_pipeline():
    print("STARTING DATA PIPELINE")

    try:
        extract_main()
        transform_main()
        load_main()
    except Exception as e:
        print("Pipeline failed")
        raise e

    print("PIPELINE FINISHED SUCCESSFULLY")


if __name__ == "__main__":
    run_pipeline()
