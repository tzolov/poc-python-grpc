from concurrent import futures
import logging

import grpc

import message_service_pb2
import message_service_pb2_grpc


class MessageService(message_service_pb2_grpc.MessagingServiceServicer):
    def requestReply(self, request, context):
        print('Server received: %s' % request.payload.decode())
        return message_service_pb2.Message(payload=str.encode(request.payload.decode().upper()))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_service_pb2_grpc.add_MessagingServiceServicer_to_server(MessageService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    print("gRPC server started on port: 50051 ...")
    serve()
