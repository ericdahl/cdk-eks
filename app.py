#!/usr/bin/env python3

from aws_cdk import core

from cdk_eks.cdk_eks_stack import CdkEksStack


app = core.App()
CdkEksStack(app, "cdk-eks")

app.synth()
