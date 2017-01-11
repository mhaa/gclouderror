import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import google.cloud.grpc.logging.v2.logging_metrics_pb2 as google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2
import google.cloud.grpc.logging.v2.logging_metrics_pb2 as google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2
import google.cloud.grpc.logging.v2.logging_metrics_pb2 as google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2
import google.cloud.grpc.logging.v2.logging_metrics_pb2 as google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2
import google.cloud.grpc.logging.v2.logging_metrics_pb2 as google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2
import google.cloud.grpc.logging.v2.logging_metrics_pb2 as google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2
import google.cloud.grpc.logging.v2.logging_metrics_pb2 as google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2
import google.cloud.grpc.logging.v2.logging_metrics_pb2 as google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2
import google.cloud.grpc.logging.v2.logging_metrics_pb2 as google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2
import google.protobuf.empty_pb2 as google_dot_protobuf_dot_empty__pb2


class MetricsServiceV2Stub(object):
  """Service for configuring logs-based metrics.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListLogMetrics = channel.unary_unary(
        '/google.logging.v2.MetricsServiceV2/ListLogMetrics',
        request_serializer=google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2.ListLogMetricsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2.ListLogMetricsResponse.FromString,
        )
    self.GetLogMetric = channel.unary_unary(
        '/google.logging.v2.MetricsServiceV2/GetLogMetric',
        request_serializer=google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2.GetLogMetricRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2.LogMetric.FromString,
        )
    self.CreateLogMetric = channel.unary_unary(
        '/google.logging.v2.MetricsServiceV2/CreateLogMetric',
        request_serializer=google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2.CreateLogMetricRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2.LogMetric.FromString,
        )
    self.UpdateLogMetric = channel.unary_unary(
        '/google.logging.v2.MetricsServiceV2/UpdateLogMetric',
        request_serializer=google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2.UpdateLogMetricRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2.LogMetric.FromString,
        )
    self.DeleteLogMetric = channel.unary_unary(
        '/google.logging.v2.MetricsServiceV2/DeleteLogMetric',
        request_serializer=google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2.DeleteLogMetricRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class MetricsServiceV2Servicer(object):
  """Service for configuring logs-based metrics.
  """

  def ListLogMetrics(self, request, context):
    """Lists logs-based metrics.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLogMetric(self, request, context):
    """Gets a logs-based metric.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateLogMetric(self, request, context):
    """Creates a logs-based metric.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateLogMetric(self, request, context):
    """Creates or updates a logs-based metric.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteLogMetric(self, request, context):
    """Deletes a logs-based metric.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MetricsServiceV2Servicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListLogMetrics': grpc.unary_unary_rpc_method_handler(
          servicer.ListLogMetrics,
          request_deserializer=google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2.ListLogMetricsRequest.FromString,
          response_serializer=google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2.ListLogMetricsResponse.SerializeToString,
      ),
      'GetLogMetric': grpc.unary_unary_rpc_method_handler(
          servicer.GetLogMetric,
          request_deserializer=google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2.GetLogMetricRequest.FromString,
          response_serializer=google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2.LogMetric.SerializeToString,
      ),
      'CreateLogMetric': grpc.unary_unary_rpc_method_handler(
          servicer.CreateLogMetric,
          request_deserializer=google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2.CreateLogMetricRequest.FromString,
          response_serializer=google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2.LogMetric.SerializeToString,
      ),
      'UpdateLogMetric': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateLogMetric,
          request_deserializer=google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2.UpdateLogMetricRequest.FromString,
          response_serializer=google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2.LogMetric.SerializeToString,
      ),
      'DeleteLogMetric': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteLogMetric,
          request_deserializer=google_dot_cloud_dot_grpc_dot_logging_dot_v2_dot_logging__metrics__pb2.DeleteLogMetricRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.logging.v2.MetricsServiceV2', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
