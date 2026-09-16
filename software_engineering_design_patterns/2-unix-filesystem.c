// Open a file, given a path and optional extra flags
int open(const char* path, int flags, mode_t permissions);

// Read a set number of bytes from the file
ssize_t read(int fd, void* buffer, size_t count);

// Write a given text to the file
ssize_t write(int fd, const void* buffer, size_t count);

// Go to a specific position in the file
off_t lseek(int fd, off_t offset, int referencePosition);

// Close the file
int close(int fd);
