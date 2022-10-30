from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2, EC2AutoScaling
from diagrams.aws.network import Route53,VPC, PrivateSubnet, PublicSubnet, InternetGateway, NATGateway, ElbApplicationLoadBalancer
from diagrams.onprem.compute import Server


# Variables
title = "VPC with 1 public subnet for the Windows server"
outformat = "png"
filename = "aws_windows_server"
direction = "TB"


with Diagram(
    name=title,
    direction=direction,
    filename=filename,
    outformat=outformat,
) as diag:
    # Non Clustered
    user = Server("user")

    # Cluster 
    with Cluster("aws"):
        with Cluster("vpc"):
            igw_gateway = InternetGateway("igw")
    
            with Cluster("Availability Zone: eu-north-1a \n\n  "):
                # Subcluster 
                with Cluster("subnet_public1"):
                     Windows_server = EC2("Windows_server")

    # Diagram

    user >> Windows_server 


diag
