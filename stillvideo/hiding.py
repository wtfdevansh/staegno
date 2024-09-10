def hiding_data(binary_message , frame):
    message_index = 0
    message_length = len(binary_message)

    
    flat_frame = frame.flatten()

    for i in range(0, len(flat_frame)):
        if message_index < message_length:
           
            flat_frame[i] = (flat_frame[i] & 254) | int(binary_message[message_index])
            message_index += 1
        else:
            break

    
    frame_with_message = flat_frame.reshape(frame.shape)
    return frame_with_message


