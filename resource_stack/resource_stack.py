from aws_cdk import (
    Stack,
    aws_sqs as sqs,
    Duration,
    aws_lambda as function_lambda,
    aws_s3 as s3
)
from constructs import Construct


class ResourceStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        queue = sqs.Queue(
            self, "AWSCDKCodePipelineappDemoQueue",
            visibility_timeout=Duration.seconds(300),
            queue_name="demo_queue"
        )
        function = function_lambda.Function(self,
                                            "DemoCDKGITHUBLambda",
                                            function_name="codepipeline_lambda",
                                            runtime=function_lambda.Runtime.PYTHON_3_9,
                                            code=function_lambda.Code.from_asset('./lambda_code_demo'),
                                            handler="demo_lambda.lambda_handler")

        bucket = s3.Bucket(self, "MyfirstBucket", versioned=True,
                           bucket_name="demo-bucket-beyond-the-cloud-98979867",
                           block_public_access=s3.BlockPublicAccess.BLOCK_ALL)
