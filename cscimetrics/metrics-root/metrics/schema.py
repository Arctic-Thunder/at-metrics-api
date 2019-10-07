import graphene
from graphene_django import DjangoObjectType
from .models import *
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay.node.node import from_global_id


class MetricNode(DjangoObjectType):
    class Meta:
        model = Metric
        filter_fields = ['timestamp']
        interfaces = (graphene.relay.Node,)

# Define Mutation Class
class CreateMetric(graphene.Mutation):
    name = graphene.String()
    data = graphene.String()
    ok = graphene.Boolean()

    # Data that can be sent to server
    class Arguments:
        name = graphene.String()
        data = graphene.String()

    # Create link in database
    def mutate(root, info, name, data):
        metric = Metric(
            name=name,
            data=data
        )
        metric.save()
        ok = True
        
        return CreateMetric(name=metric.name, data=metric.data, ok=ok)


# Define Update Class
class UpdateMetric(graphene.relay.ClientIDMutation):
    metric = graphene.Field(MetricNode)

    class Input:
        id = graphene.String()
        name = graphene.String()
        data = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        metric = Metric.objects.get(
            pk=from_global_id(input.get('id'))[1]
        )
        metric.name = input.get('name')
        metric.data = input.get('data')
        metric.save()
        
        return UpdateMetric(metric=metric)


# Define Delete Class
class DeleteMetric(graphene.relay.ClientIDMutation):
    metric = graphene.Field(MetricNode)

    class Input:
        id = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        metric = Metric.objects.get(
            pk=from_global_id(input.get('id'))[1]
        )

        metric.delete()
        return DeleteMetric(metric=metric)

# Create Mutation Class
class Mutation(graphene.AbstractType):
    create_metric = CreateMetric.Field()
    update_metric = UpdateMetric.Field()
    delete_metric = DeleteMetric.Field()
    

class Query(object):
    metric = graphene.relay.Node.Field(MetricNode)
    all_metrics = DjangoFilterConnectionField(MetricNode)
