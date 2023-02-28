import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_codepipeline.aws_codepipeline_stack import AwsCodepipelineStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_codepipeline/aws_codepipeline_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCodepipelineStack(app, "aws-codepipeline")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
