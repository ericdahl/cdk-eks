from aws_cdk import core
import aws_cdk.aws_eks as eks


class CdkEksStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cluster = eks.Cluster(self, "cdk-eks", version=eks.KubernetesVersion.V1_18)

        cluster.add_manifest('hello', {
            "apiVersion": 'v1',
            "kind": 'Pod',
            "metadata": {
                "name": 'mypod'
            },
            "spec": {
                "containers": [
                    {
                        "name": 'hello',
                        "image": 'paulbouwer/hello-kubernetes:1.10',
                        "ports": [
                            {
                                "containerPort": 8080
                            }
                        ]
                    }
                ]
            }
        })

