# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.documentai_v1beta1.proto import (
    document_understanding_pb2 as google_dot_cloud_dot_documentai__v1beta1_dot_proto_dot_document__understanding__pb2,
)
from google.longrunning import (
    operations_pb2 as google_dot_longrunning_dot_operations__pb2,
)


class DocumentUnderstandingServiceStub(object):
    """Service to parse structured information from unstructured or semi-structured
  documents using state-of-the-art Google AI such as natural language,
  computer vision, and translation.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.BatchProcessDocuments = channel.unary_unary(
            "/google.cloud.documentai.v1beta1.DocumentUnderstandingService/BatchProcessDocuments",
            request_serializer=google_dot_cloud_dot_documentai__v1beta1_dot_proto_dot_document__understanding__pb2.BatchProcessDocumentsRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )


class DocumentUnderstandingServiceServicer(object):
    """Service to parse structured information from unstructured or semi-structured
  documents using state-of-the-art Google AI such as natural language,
  computer vision, and translation.
  """

    def BatchProcessDocuments(self, request, context):
        """LRO endpoint to batch process many documents.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_DocumentUnderstandingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "BatchProcessDocuments": grpc.unary_unary_rpc_method_handler(
            servicer.BatchProcessDocuments,
            request_deserializer=google_dot_cloud_dot_documentai__v1beta1_dot_proto_dot_document__understanding__pb2.BatchProcessDocumentsRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        )
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.documentai.v1beta1.DocumentUnderstandingService",
        rpc_method_handlers,
    )
    server.add_generic_rpc_handlers((generic_handler,))
