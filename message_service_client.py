from __future__ import print_function
import logging
import sys

import grpc

import message_service_pb2
import message_service_pb2_grpc


def run(send_message):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = message_service_pb2_grpc.MessagingServiceStub(channel)
        response = stub.requestReply(message_service_pb2.Message(payload=str.encode(send_message)))
    print("Client received: " + response.payload.decode())


if __name__ == '__main__':
    logging.basicConfig()
    run(sys.argv[1])
