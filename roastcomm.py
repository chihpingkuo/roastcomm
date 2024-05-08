#!/usr/bin/env python
"""
RoastComm
"""

import pymodbus.client as ModbusClient
from pymodbus import (
    ExceptionResponse,
    Framer,
    ModbusException,
    pymodbus_apply_logging_config,
)
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder


def run_sync_simple_client(port, framer=Framer.RTU):
    """Run sync client."""
    # activate debugging
    pymodbus_apply_logging_config("DEBUG")

    print("get client")

    client = ModbusClient.ModbusSerialClient(
        port,
        framer=framer,
        # timeout=10,
        # retries=3,
        # retry_on_empty=False,
        # strict=True,
        baudrate=9600,
        bytesize=8,
        parity="N",
        stopbits=1,
        # handle_local_echo=False,
    )

    print("connect to server")
    client.connect()

    print("get and verify data")
    try:
        rr = client.read_holding_registers(address=18176, count=1, slave=1)
    except ModbusException as exc:
        print(f"Received ModbusException({exc}) from library")
        client.close()
        return
    if rr.isError():
        print(f"Received Modbus library error({rr})")
        client.close()
        return
    if isinstance(rr, ExceptionResponse):
        print(f"Received Modbus library exception ({rr})")
        # THIS IS NOT A PYTHON EXCEPTION, but a valid modbus message
        client.close()

    decoder = BinaryPayloadDecoder.fromRegisters(
        rr.registers, byteorder=Endian.BIG, wordorder=Endian.BIG
    )

    print(decoder.decode_16bit_int()*0.1)

    print("close connection")
    client.close()


if __name__ == "__main__":
    run_sync_simple_client("COM3")
