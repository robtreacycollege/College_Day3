#!/bin/bash

# This is where you have cloned out the https://github.com/grpc/grpc repository
# And built gRPC Python.
# ADJUST THIS PATH TO WHERE YOUR ACTUAL LOCATION IS
GRPC_ROOT=../grpc

#$GRPC_ROOT/python2.7_virtual_environment/bin/python server.py
#$GRPC_ROOT/python2.7_virtual_environment/bin/python add_person_server.py
#$GRPC_ROOT/python2.7_virtual_environment/bin/python list_person_server.py
$GRPC_ROOT/python2.7_virtual_environment/bin/python client_list_person_server.py