import graphene
from graphene_django import DjangoObjectType
from .models import *
from graphene_django.filter import DjangoFilterConnectionField


class MetricNode(DjangoObjectType):
    class Meta:
        model = Metric
        filter_fields = ['timestamp', 'type']
        interfaces = (graphene.relay.Node,)

# Define Mutation Class
class CreateMetric(graphene.Mutation):
    name = graphene.String()
    description = graphene.String()
    ok = graphene.Boolean()

    # Data that can be sent to server
    class Arguments:
        name = graphene.String()
        description = graphene.String()

    # Create link in database
    def mutate(root, info, name, description):
        metric = Metric(
            name=name,
            description=description,
            type=MetricType(
                name="Test",
            )
        )
        metric.save()
        ok = True
        
        return CreateMetric(name=metric.name, description=metric.description, ok=ok)

# Create Mutation Class
class Mutation(graphene.AbstractType):
    create_metric = CreateMetric.Field()
    

class Query(object):
    metric = graphene.relay.Node.Field(MetricNode)
    all_metrics = DjangoFilterConnectionField(MetricNode)
