#!/usr/bin/env python3

from aws_cdk import core

from eks.cdk_eks_stack import CdkEksStack


app = core.App()
CdkEksStack(app, "cdk-eks")

app.synth()
