# Get pointer copy
ptr_copy = get_copy(obj)

# Is obj free?
if is_unlocked(ptr_copy):
    # return current obj
    return obj

# Already a copy?
if is_copy(ptr_copy):
    # return obj
    return obj

thread_id = get_thread_id(ptr_copy)
# Locked by current ctx
if thread_id == ctx.thread_id:
    # Return copy 
    return ptr_copy
