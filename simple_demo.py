import simple_pb2 as simple_pb

simple_message = simple_pb.SimpleMessage()
simple_message.id = 123
simple_message.is_simple = True
simple_message.name = "This is a simple Message"
sample_list = simple_message.sample_list
sample_list.append(3)
sample_list.append(4)
sample_list.append(5)

print(simple_message)
print(sample_list)

with open("simple.bin", "wb") as f:
    bytesAsString = simple_message.SerializeToString()
    f.write(bytesAsString)

with open("simple.bin", "rb") as f:
    simple_message_read = simple_pb.SimpleMessage().FromString(f.read())

print(simple_message_read)
print("Is simple?: " + str(simple_message_read.is_simple))