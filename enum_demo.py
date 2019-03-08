import enum_example_pb2 as enum_example_pb2

enum_message = enum_example_pb2.EnumMessage()
enum_message.id = 345
enum_message.day_of_the_week = enum_example_pb2.THURSDAY

print(enum_message)

with open("enum.bin", "wb") as f:
    f.write(enum_message.SerializeToString())
    print("Wrote to a file")

with open("enum.bin", "rb") as f:
    enum_message_read = enum_example_pb2.EnumMessage().FromString(f.read())

print(enum_message_read)