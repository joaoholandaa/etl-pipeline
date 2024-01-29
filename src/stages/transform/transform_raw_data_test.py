from src.stages.contracts.mocks.extract_contract import extract_contract_mock
from .transform_raw_data import TransformRawData

class test_transform():
    transform_raw_data = TransformRawData()
    transformed_information = transform_raw_data.transform(extract_contract_mock)
    print()
    print(transformed_information)