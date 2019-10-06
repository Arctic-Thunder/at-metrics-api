import graphene
import metrics.schema

class Query(metrics.schema.Query, graphene.ObjectType):
    pass

class Mutation(metrics.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)