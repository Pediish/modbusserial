import minimalmodbus
import serial

def read_modbus_registers(port, slave_address, start_address, count):
    try:

        instrument = minimalmodbus.Instrument(port, slave_address)


        instrument.serial.baudrate = 19200
        instrument.serial.bytesize = 8
        instrument.serial.parity = serial.PARITY_NONE
        instrument.serial.stopbits = 1
        instrument.serial.timeout = 1

        instrument.mode = minimalmodbus.MODE_RTU


        registers = instrument.read_registers(start_address, count)
        return registers

    except minimalmodbus.NoResponseError:
        print("No response from the slave device.")
    except minimalmodbus.InvalidResponseError:
        print("Received invalid response from the slave device.")
    except minimalmodbus.IllegalRequestError as e:
        print(f"Illegal request: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


port = '/dev/ttyS2'
slave_address = 9
start_address = 0
count = 20


registers = read_modbus_registers(port, slave_address, start_address, count)
if registers:
    print(f"Register values: {registers}")
